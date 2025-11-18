#include <Windows.h>
#include <winbase.h>
#include <ioapiset.h>
#include <fileapi.h>
#include <iostream>
#include <sstream>
#include <ntddscsi.h>
#include <minwindef.h>
#include <cstring>
#include <ntdddisk.h>
#include <string>
#include <winioctl.h>
#include <vector>
#include <mi.h>
#include <iomanip>
#include <csignal>


// targeting Windows 7 or above.
#define WINVER 0x0601
#define _WIN32_WINNT 0x0601
// reducing the size of executable by excluding various unnecessary objects.
#define WIN32_LEAN_AND_MEAN
#define byte unsigned char

// GLOBALS (should have handles here)
HANDLE physicalDiskHandle = nullptr;
MI_Application mi_App_Handle = MI_APPLICATION_NULL;
MI_Session mi_session = MI_SESSION_NULL;
MI_Instance* msft_vol_instance = NULL;
MI_Instance* optimize_func_params_instance = NULL;
MI_Operation optimizeFuncOperation = MI_OPERATION_NULL;

void __cdecl SIGINTHandler(const int SIG) {
	std::cout << "INFO: ata_trim process received termination signal, Will terminate safely...\n";
	// ... implement code for closing handles here ...
	// deleting operation instance
	if (
		(optimizeFuncOperation.reserved1 != 0) && (optimizeFuncOperation.reserved2 != 0)
		) {
		if (MI_Operation_Close(&optimizeFuncOperation) != MI_RESULT_OK) {
			std::cerr << "error: failed to close MI Operation!, an existing ReTrim could be running\n" <<
				"If the issue still persists, Please reboot your computer.\n";
		}
	}
	// deleting Parameters instance
	if (optimize_func_params_instance != NULL) {
		// our Parameters instance is initialized
		// therefore we must delete it
		if (MI_Instance_Delete(optimize_func_params_instance) != MI_RESULT_OK) {
			std::cerr << "error: failed to delete Parameters instance!\n";
		}
	}
	// deleting MSFT_Volume instance
	if (msft_vol_instance != NULL) {
		// our MSFT_Volume instance has been initialized
		// therefore we must close it
		if (MI_Instance_Delete(msft_vol_instance) != MI_RESULT_OK) {
			std::cerr << "error: failed to delete MSFT_Volume instance!\n";
		}
	}
	// closing MI Application Session in mi_session
	if (
		(mi_session.reserved1 != 0) && (mi_session.reserved2 != 0)
		) {
		if (MI_Session_Close(&mi_session, 0, NULL) != MI_RESULT_OK) {
			std::cerr << "error: failed to close MI Session handle!, Please restart your PC!\n";
		}
	}
	// closing MI Application Handle in mi_App_Handle
	if ((mi_App_Handle.reserved1 != 0) && (mi_App_Handle.reserved2 != 0)) {
	// we can close the application handle now.
		if (MI_Application_Close(&mi_App_Handle) != MI_RESULT_OK) {
			std::cerr << "error: failed to close MI Application Handle!, Please restart your PC!\n";
		}
	}
	// closing the physical disk handle (conditionally)
	if (
		((physicalDiskHandle != nullptr) && (physicalDiskHandle != INVALID_HANDLE_VALUE))
		) {
		if (CloseHandle(physicalDiskHandle) == 0)
			std::cerr << "error: failed to close physical disk handle!, Please restart your PC!\n";
	}
	exit(12); // exit code 12 is for kbd interrupt
	return;
}




int main(int argc, char* argv[]) {
	// adding SIGINT handlers.
	signal(SIGINT, SIGINTHandler);
	signal(SIGTERM, SIGINTHandler);

	LPCSTR physical_disk;
	if (argc > 1) {
		physical_disk = argv[1];
		std::cout << "Physical Disk is " << physical_disk << '\n';
	}
	else {
		std::cerr << "Failure: missing physical disk address.\n";
		return 1;
	}
	// create a handle to physical disk in physical_disk (argv[1]).
	physicalDiskHandle = CreateFileA(
		static_cast<LPCSTR>(physical_disk),
		GENERIC_READ | GENERIC_WRITE,
		FILE_SHARE_READ | FILE_SHARE_WRITE,
		NULL,
		OPEN_EXISTING,
		FILE_FLAG_NO_BUFFERING,
		NULL
	);
	if (physicalDiskHandle == INVALID_HANDLE_VALUE) {
		std::cerr << "error: failed to open handle to physical disk " << physical_disk << ", error code: " <<
			GetLastError() << '\n';
		return 2;
	}
	// we need to check if physical_disk supports TRIM or not.
	STORAGE_PROPERTY_ID storPropertyID = StorageDeviceTrimProperty;
	STORAGE_QUERY_TYPE storPropertyQueryType = PropertyStandardQuery;
	STORAGE_PROPERTY_QUERY spqStruct;
	spqStruct.PropertyId = storPropertyID;
	spqStruct.QueryType = storPropertyQueryType;
	DEVICE_TRIM_DESCRIPTOR deviceTrimDescOutput = { 0 };
	DWORD queryIoCtlBytesReturned = 0;
	BOOL queryTrimDevIoCtlResult = DeviceIoControl(
		physicalDiskHandle,
		IOCTL_STORAGE_QUERY_PROPERTY,
		&spqStruct,
		sizeof(spqStruct),
		&deviceTrimDescOutput,
		sizeof(deviceTrimDescOutput),
		&queryIoCtlBytesReturned,
		nullptr
	);
	if (queryTrimDevIoCtlResult == 0) {
		std::cerr << "error: failed to query disk properties, error code: " << GetLastError() << '\n';
		return 3;
	}
	BOOLEAN isTrimSupported = deviceTrimDescOutput.TrimEnabled;
	if (isTrimSupported) {
		std::cout << "disk " << physical_disk << " reports TRIM Support!\n";
	}
	else {
		if ((argc >= 3) && (strcmp(argv[2], "--bypassChecks") == 0)) {
			std::cout << "TRIM Check is explicitly disabled by the user!\n";
		}
		else {
			std::cerr << "disk " << physical_disk << " reports no ATA TRIM command support!\n";
			return 4;
		}
	}
	// the actual disk trimming process.
	// now we need to obtain volume letter from argv.
	std::string volLetterToTrim;
	switch (argc) {
	case 3:
		if (static_cast<std::string>(argv[2]).find('-') == std::string::npos) {
			volLetterToTrim = argv[2];
			break;
		}
		// if it reaches the code here, it means that a volume letter has been
		// omitted when the program was called.
		goto error;
		break;
	case 4:
		if (static_cast<std::string>(argv[2]).find('-') == std::string::npos) {
			volLetterToTrim = argv[2];
			break;
		}
		if (static_cast<std::string>(argv[3]).find('-') == std::string::npos) {
			volLetterToTrim = argv[3];
			break;
		}
		// if it reaches the code here, then invalid argv is found
		goto error;
		break;
	default:
	error:
		std::cerr << "error: invalid arguments: missing volume letter to issue trim commands onto!\n";
		return 245; // 245 is for a missing volume letter to issue trim commands onto.
	}
	std::cout << "Trimming volume: " << volLetterToTrim << ", on disk: " << physical_disk << "...\n";

	// we will be calling Windows's built-in Optimize command via
	// Windows Management Infrastructure (MI)
	std::string appGUID = "CE2D78E1-887D-482B-9CB6-FAA66E608FAA";

	MI_Result miRes = MI_Application_Initialize(
		0,
		(wchar_t*)appGUID.c_str(),
		NULL,
		&mi_App_Handle
	);

	if (miRes != MI_RESULT_OK) {
		std::cerr << "Failed to initialize a MI App Handle, Error code is: " << miRes << '\n';
		if (CloseHandle(physicalDiskHandle) == 0) {
			std::cerr << "Failed to close disk handle!, Error code: " << GetLastError() << '\n' <<
				"You will not be able to run ata_trim operation again until you restart your computer!\n";
		}
		return 5;
	}
	// our MI App handle is initialized!
	// at this point, we must not forget to close the application handle

	miRes = MI_Application_NewSession(
		&mi_App_Handle,
		NULL,
		NULL,
		NULL,
		NULL,
		NULL,
		&mi_session
	);
	if (miRes != MI_RESULT_OK) {
		std::cerr << "Failed to initialize a new MI Session, Error code is: " << miRes << '\n';
		// we must close our MI Application handle.
		if (MI_Application_Close(&mi_App_Handle) != MI_RESULT_OK) {
			std::cerr << "Fatal Error occured!, Failed to handle exception with initializing a MI Session\n";
		}
		if (CloseHandle(physicalDiskHandle) == 0) {
			std::cerr << "Fatal Error occured!, Failed to close physical disk handle!\n";
		}
		return 6;
	}
	// we need to make a new instance of the class MSFT_Volume
	// first so we can pass parameters to the function Optimize
	// that we are trying to call using MI_Session_Invoke

	miRes = MI_Application_NewInstance(&mi_App_Handle,
		L"MSFT_Volume",
		NULL, // we don't need to use RTTI for now
		&msft_vol_instance
	);
	if (miRes != MI_RESULT_OK) {
		std::cerr << "error: Failed to make a new instance of MSFT_Volume!, error code: " << miRes << '\n' <<
			"If you are a user and you are seeing this during normal functionality of this program, please create an issue with this log in the Github repository of Temp_Cleaner GUI\n";
		// we must close application and session instances (session goes first)
		if (MI_Session_Close(&mi_session, NULL, NULL) != MI_RESULT_OK)
			std::cerr << "error: Failed to handle MSFT_Volume instance creation exception, stage Close MI Session handle\n";
		if (MI_Application_Close(&mi_App_Handle) != MI_RESULT_OK)
			std::cerr << "error: failed to handle MSFT_Volume instance creation exception, stage Close MI Application handle\n";
		// we must close the physical disk handle too.
		if (CloseHandle(physicalDiskHandle) == 0)
			std::cerr << "error: failed to handle MSFT_Volume instance creation exception, stage Close Physical Disk handle!\n";
		return 7;
	}
	// now that we have our MSFT_Volume instance ready, we need to add option
	// VolumeLetter to it.
	MI_Value volLetterMiValue;
	volLetterMiValue.char16 = (char16_t)volLetterToTrim.c_str();
	miRes = MI_Instance_AddElement(msft_vol_instance,
		L"DriveLetter",
		&volLetterMiValue,
		MI_CHAR16,
		MI_FLAG_KEY
	);
	if (miRes != MI_RESULT_OK) {
		std::cerr << "error: Failed to add element DriveLetter to MI Instance MSFT_Volume!, error code is: " <<
			miRes << '\n';
		// we must close instance to MSFT_Volume, then session instance
		// then application handle.
		if (MI_Instance_Delete(msft_vol_instance) != MI_RESULT_OK)
			std::cerr << "error: Failed to delete MI Instance MSFT_Volume!: \n";
		if (MI_Session_Close(&mi_session, NULL, NULL) != MI_RESULT_OK)
			std::cerr << "error: Failed to close MI Session instance!\n";
		if (MI_Application_Close(&mi_App_Handle) != MI_RESULT_OK)
			std::cerr << "error: Failed to close MI Application handle!\n";
		if (CloseHandle(physicalDiskHandle) == 0)
			std::cerr << "error: Failed to close physical disk handle\n";
		return 8;
	}
	
	miRes = MI_Application_NewInstance(
		&mi_App_Handle,
		L"Parameters",
		NULL,
		&optimize_func_params_instance
	);
	if (miRes != MI_RESULT_OK) {
		std::cerr << "error: Failed to create a parameters instance for MSFT_Volume_Optimize!, error code is: " <<
			miRes << '\n';
		// we must close instance to MSFT_Volume, then session instance
		// then application handle.
		if (MI_Instance_Delete(msft_vol_instance) != MI_RESULT_OK)
			std::cerr << "error: Failed to delete MI Instance MSFT_Volume!: \n";
		if (MI_Session_Close(&mi_session, NULL, NULL) != MI_RESULT_OK)
			std::cerr << "error: Failed to close MI Session instance!\n";
		if (MI_Application_Close(&mi_App_Handle) != MI_RESULT_OK)
			std::cerr << "error: Failed to close MI Application handle!\n";
		if (CloseHandle(physicalDiskHandle) == 0)
			std::cerr << "error: Failed to close physical disk handle!\n";
		return 9;
	}
	// now that we have our instance of MSFT_Volume_Optimize
	// we need to add the retrim option to it so it will instruct 
	// the optimize function that we want to run the retrim command.
	MI_Value trueMiValue;
	trueMiValue.boolean = MI_TRUE;
	miRes = MI_Instance_AddElement(
		optimize_func_params_instance,
		L"ReTrim",
		&trueMiValue,
		MI_BOOLEAN,
		0
	);
	// now that we have got all instances ready to use, we can invoke
	// the Optimize function now!
	// NOTE from Claude: using callbacks will make the optimize function run
	// asynchronously, which is something we don't want to.

	MI_Session_Invoke(
		/*Session*/ &mi_session,
		/*flags*/ 0,
		/*MI Operation options - Options*/ NULL,
		/* Namespace Name */ L"Root\\Microsoft\\Windows\\Storage",
		/* Class Name */ L"MSFT_Volume",
		/* Method Name */ L"Optimize",
		/* Inbound Instance (the MSFT_Volume instance) */ msft_vol_instance,
		/* Inbound Properties */ optimize_func_params_instance,
		/* Callbacks */ NULL,
		/* [out] Operation instance or handle */ &optimizeFuncOperation
	);
	// since our operation doesn't have any callbacks associated with it
	// it will be synchronous therefore we need to make calls to retrieve
	// its active instance to join/wait the current retrim operation.

	/* For displaying operation result & waiting for the retrim operation */
	const MI_Instance* resultInstance = NULL;
	MI_Boolean moreResultsAvailable = MI_TRUE;
	MI_Result OptimizeFuncCallResult;
	const MI_Char* OptimizeFuncCallErrorMsg = NULL;
	const MI_Instance* completionDetails = NULL;
	while (moreResultsAvailable == MI_TRUE) {
	MI_Operation_GetInstance( // we don't need to store the return value of this function call.
		/* MI operation handle */ &optimizeFuncOperation,
		&resultInstance, /* MI operation result instance, Note the result instance is only valid
							until any of these MI_Operation_GetInstance(), MI_Operation_Close() are called */
		&moreResultsAvailable, /* Are there any more results available?, The value stored in the pointed to
								variable should be MI_FALSE or else any attempts to close the Session will just
								cause a deadlock/application hang */
		&OptimizeFuncCallResult, /* A pointer to a MI_Result variable which will store the result of the operation */
		&OptimizeFuncCallErrorMsg, /* A pointer to a MI_Char array which will store the error message if the operation fails */
		&completionDetails /* A pointer to a MI_Instance object that contains information about the completion of the process. */
		);
	
	}
	if (OptimizeFuncCallResult != MI_RESULT_OK) {
			std::cerr << "error: Failed to trim volume " << volLetterToTrim << " ";
			std::wcerr << OptimizeFuncCallErrorMsg;
			std::cerr << '\n';
	}



	/* Closing MI App handles and other stuff 
	   Actual program functionality should reside above (not below)
	   this block of code.
	*/
	std::cout << "INFO: All pending operations has been completed!, Releasing all handles and cleaning up...\n";
	// before doing anything, we first have to close our operation
	miRes = MI_Operation_Close(&optimizeFuncOperation);
	if (miRes != MI_RESULT_OK) {
		std::cerr << "Failed to close MI_Operation handle!, Error code is: " << miRes << '\n';
		return 255;
	}
	// before closing our MI Session, we need to delete instances of msft volume
	// and msft volume optimize
	miRes = MI_Instance_Delete(msft_vol_instance);
	if (miRes != MI_RESULT_OK) {
		std::cerr << "Failed to delete instance of MSFT_Volume, Error code is: " << miRes << '\n';
		return 255;
	}
	miRes = MI_Instance_Delete(optimize_func_params_instance);
	if (miRes != MI_RESULT_OK) {
		std::cerr << "Failed to delete instance of Parameters, Error code is: " << miRes << '\n';
		return 255;
	}
	
	miRes = MI_Session_Close(&mi_session, 0, NULL);
	if (miRes != MI_RESULT_OK) {
		std::cerr << "Failed to close MI Session handle!, This indicates an error that should never be ignored\nIf you as a user are seeing this, please create an issue with this Log IMMEDIATELY in the official project Github repository\nError code is: " <<
			miRes << '\n';
		return 255;
	}

	miRes = MI_Application_Close(&mi_App_Handle);
	if (miRes != MI_RESULT_OK) {
		std::cerr << "Failed to close MI Application handle!, This indicates an error that should never be ignored\nIf you as a user are seeing this, please create an issue with this Log IMMEDIATELY in the official project Github repository\nError code is: " <<
			miRes << '\n';
		return 255;
	}
	if (CloseHandle(physicalDiskHandle) == 0) {
		std::cerr << "Failed to close handle to physical disk: " << physical_disk << ", Please report this issue in the official Github repository of Temp_Cleaner GUI\nError code is: " <<
			GetLastError() << '\n';
		return 255;
	}
	// all done, all handles are supposed to be closed, so now it's safe to exit with code 0
	std::cout << "INFO: All handles have been successfully closed!\n";
	return 0;
}