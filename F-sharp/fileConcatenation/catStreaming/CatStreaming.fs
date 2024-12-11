module CatStreaming
open System.IO


let readBytes (count:int) (buffer:byte[]) (fs:FileStream) : int =
    let x = fs.Read(buffer, 0 ,count)
    printfn "%A" x
    x


let writeBytes (count:int) (buffer:byte[]) (fs:FileStream) : unit =
    fs.Write(buffer, 0, count) 


let readAndWriteBytes (buffersize:int) (buffer:byte[]) (inputFilleStream:FileStream) (outputFilleStream:FileStream) =
    let rec inner () =
        let readBytes = readBytes buffersize buffer inputFilleStream
        if readBytes = 0 
        then outputFilleStream.Flush()
        else writeBytes readBytes buffer outputFilleStream |> inner
    inner () 


let openFileRead (filenameSingular:string) : FileStream =
    try
        File.OpenRead filenameSingular
    with
        _ -> raise (System.IO.FileNotFoundException())


let openFileWrite (filenameSingular:string) : FileStream option =
    try
        File.Open(filenameSingular, FileMode.Create) |> Some
    with
        _ ->
            sprintf "cat: Could not create or truncate file \"%s\" " filenameSingular
            |> System.Console.Error.WriteLine
            None


let catWithBufferSize (buffersize:int) (filenamesPlural:string[]) : int =
    let len = 3
    let buffer = Array.init buffersize (fun _ -> 0uy)
    let infiles = filenamesPlural.[..len-2] |> List.ofArray
    let outfile = filenamesPlural.[len-1]
    let ifs = List.map (fun filenameSingular -> try openFileRead filenameSingular |> Some with _ -> None) infiles
    let outputFileStream = openFileWrite outfile
    List.map Option.get ifs
    |> List.map (fun inputfile -> readAndWriteBytes buffersize buffer inputfile (Option.get(outputFileStream)))
    (Option.get(outputFileStream)).Close()
    0 // exit status
            
let cat = catWithBufferSize 32

