module tyveotteogfyrre

// A 2D vector in board coordinats 
type pos = int*int 

// Piece values 
type value = Red | Green | Blue | Yellow | Black 

type piece = value*pos 

// The board is a set of randomly organized pieces 
type state = piece list 

/// <summary> Recives a color value and returns a color compatible with canvas package </summary>
/// <param name = v> Color of type value </param>
/// <returns> Returns canvas color </returns>
let fromValue (v:value): Canvas.color= 
    match v with
        | Red -> Canvas.red 
        | Green -> Canvas.green  
        | Blue -> Canvas.blue
        | Yellow -> Canvas.yellow
        | Black -> Canvas.black 

/// <summary> Recives a color value and returns a different color </summary>
/// <param name = C> Color of type value </param>
/// <returns> Returns color based on color received </returns>
let nextColor (c:value): value=
    match c with 
        |Black -> Black
        |Red -> Green 
        |Green -> Blue 
        |Blue -> Yellow 
        |Yellow -> Black

/// <summary> Receives list of pieces and returns list of pieces with certain position </summary>
/// <param name = k> number of type int which works as a filter parameter </param>
/// <param name = s> List of pieces </param>
/// <returns> Returns list of pieces with certain position matching parameter k  </returns>
let filter (k:int)(s:state): state = 
    List.filter(fun (v, (x, y)) -> (k=y))s

/// <summary> Receives list of pieces and returns list of pieces with certain position </summary>
/// <param name = s> List of pieces </param>
/// <returns> Returns list of pieces </returns>
let rec moveUp (s:state) : state =
        match s with
            |[] -> []
            |_-> List.mapi(fun i (v,(x,y)) -> (v,(i,y)))s

/// <summary> Receives list of pieces and returns sorted list of pieces </summary>
/// <param name = s> List of pieces </param>
/// <returns> Returns sorted list of pieces </returns>
let sort (s:state) : state =
        List.sortBy(fun (_,(x,_)) -> x ) s

/// <summary> Receives list of pieces and returns rearranged list of pieces </summary>
/// <param name = s> List of pieces </param>
/// <returns> Returns rearranged list of pieces </returns>        
let rec collide (s:state) : state =
        match s with
            | [(a); (b); (c)] ->
                if fst(a) = fst(b)
                then  [nextColor(fst(b)), snd(b)] @ collide [(c)]
                else [(a)] @ collide [(b); (c)]
            | [(a); (b)] ->
                if fst(a) = fst(b)
                then [nextColor(fst(b)), snd(b)]
                else [(a); (b)]
            | [(a)] ->
                [(a)]
            |_->
                []

/// <summary> Receives list of pieces and returns sorted and rearranged list of pieces </summary>
/// <param name = s> List of pieces </param>
/// <returns> Returns sorted and rearranged list of pieces </returns>
let shiftUp (s:state) : state =
    (moveUp(collide(sort(filter 0 s)))) @ 
    (moveUp(collide(sort(filter 1 s)))) @
    (moveUp(collide(sort(filter 2 s))))

/// <summary> Receives list of pieces and returns list of pieces </summary>
/// <param name = s> List of pieces </param>
/// <returns> Returns list of pieces </returns>
let flipUD (s:state) : state =
    List.map(fun (v,(x,y)) -> (v,(2-x,y)))s

/// <summary> Receives list of pieces and returns list of pieces </summary>
/// <param name = s> List of pieces </param>
/// <returns> Returns list of pieces </returns>
let transpose (s:state) : state =
    List.map(fun (v,(x,y)) -> (v,(y,x)))s

/// <summary> Receives list of pieces and returns list of pieces </summary>
/// <param name = s> List of pieces </param>
/// <returns> Returns list of pieces </returns>
let empty (s:state) =
    [0; 1; 2] |> List.allPairs [0; 1; 2] |> List.except (List.map(fun (x,y) -> y)s) |> List.except[(1,1)]

/// <summary> Receives list of pieces and returns list of pieces </summary>
/// <param name = s> List of pieces </param>
/// <param name = c> color of type value </param>
/// <returns> Returns random piece concatenated with list of pieces </returns>
let addRandom (c:value) (s:state) : state option =
    let n = empty s
    let rnd = System.Random ()
    match n with
        | [] -> None
        |_->
            Some ((c, (n[rnd.Next (n.Length-1)]))::s)