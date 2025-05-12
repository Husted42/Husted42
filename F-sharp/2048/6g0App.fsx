open tyveotteogfyrre

#r "nuget:DIKU.Canvas, 1.0.1"
open Canvas

let w=600
let h=w 

/// <summary> Receives list of pieces and returns a canvas </summary>
/// <param name = s> List of pieces </param>
/// <returns> Returns a canvas </returns>
let draw width height (s:state) =
    let C = create width height
    let V = List.map(fun (v,(x,y)) -> do setFillBox C (fromValue v) (x*w/3,y*w/3) ((x+1)*w/3,(y+1)*w/3)) s
    C

/// <summary> Receives list of pieces and returns a canvas </summary>
/// <param name = s> List of pieces </param>
/// <param name = k> number of type key </param>
/// <returns> Returns a list of pieces </returns>
let react (s:state) (k:key): state option= 
    match getKey k with 
        |UpArrow -> Some (transpose(shiftUp(transpose s))) |> Option.get |> addRandom Red
        |DownArrow -> Some (transpose(flipUD(shiftUp(flipUD(transpose s))))) |> Option.get |> addRandom Red
        |LeftArrow -> Some (shiftUp s) |> Option.get |> addRandom Red
        |RightArrow -> Some ((flipUD(shiftUp(flipUD s)))) |> Option.get |> addRandom Red
        |_ -> None

do runApp "MegaCoolAwesomeGame" w h draw react [(Red,(0,2)); (Red,(0,1))]
