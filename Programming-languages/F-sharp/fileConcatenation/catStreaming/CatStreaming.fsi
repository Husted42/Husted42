module CatStreaming

open System.IO

/// <summary> Reads files and create a file with the data</summary>
/// <param name="buffersize"> The size of the chucks the programs reads/writes </param>
/// <param name="filenamesPlural"> The name of the file that should be read and the name of files that should be created </param>
/// <returns> a new file in main folder </returns>
val catWithBufferSize: int -> string[] -> int

// REQUIRED
val cat: (string[] -> int)

/// <summary> Read a block of bytes from fileStream and writes the data in buffer </summary>
/// <param name="count"> Decide where the buffer ends. buffer goes from offset(0) to count </param>
/// <param name="buffer"> Stores data read from fileStream. Buffer er muterbar </param>
/// <param name="fs"> the stream of files that the function reads </param>
/// <returns>Returns number of bytes in buffer</returns>
val readBytes: int -> byte[] -> FileStream -> int

/// <summary> writes a block of bytes to fileStream from buffer </summary>
/// <param name="count"> Decide where the buffer ends. buffer goes from offset(0) to count </param>
/// <param name="buffer"> Stores data read from fileStream. Buffer er muterbar </param>
/// <param name="fs"> the stream of files that the function writes to </param>
/// <returns>Returns number of bytes in buffer</returns>
val writeBytes: int -> byte[] -> FileStream -> unit

/// <summary> Reads input files and writes the data in output files</summary>
/// <param name="buffersize"> Decides the size of bufffer </param>
/// <param name="buffer"> buffer with the lenght of buffersize </param>
/// <param name="inputFilleStream"> the stream of files that the function reads </param>
/// <param name="outputFilleStream"> the stream of files that the function writes to </param>
/// <returns> unit </returns>
val readAndWriteBytes: int -> byte[] -> FileStream -> FileStream -> unit

/// <summary> Opens a file that needs to be read</summary>
/// <param name="filenameSingular"> The name of a file that needs to be read </param>
/// <returns> the opend file (FileStream) </returns>
val openFileRead: string -> FileStream

/// <summary> Creates the output file</summary>
/// <param name="filenameSingular"> The name of the file that is created </param>
/// <returns> the new file (FileStream option) </returns>
val openFileWrite: string -> FileStream option
