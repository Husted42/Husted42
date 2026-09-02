(*-- Types --*)
type pos = int*int

(*-- Variables --*)
let src: pos = (3,4)
let tgt: pos = (1,1)

(*-- Functions --*)
/// <summary> Receives a pair coordinates and returns the distance between those two coordiantes. </summary>
/// <param name = a> The first set of coordinates (p1) </param>
/// <param name = b> The second set of coordinates (p2) </param>
/// <returns> Returns distance between two random coordiantes </returns>
let dist a b =
    let x1 = ((fst b) - (fst a)) * ((fst b) - (fst a))
    let x2 = ((snd b) - (snd a)) * ((snd b) - (snd a))
    x1 + x2

/// <summary> Receives a pair coordinates and returns the distance between those two coordiantes. </summary>
/// <param name = a> The first set of coordinates (p1) </param>
/// <param name = b> The second set of coordinates (p2) </param>
/// <returns> Returns a list of possible routes that are equal to or shorter than the distance from a to b </returns>
let candidates a b : pos list = 
    let route1 = (((fst a) + 1),(snd a))
    let route2 = (((fst a) - 1),(snd a))
    let route3 = ((fst a), ((snd a) + 1))
    let route4 = ((fst a), ((snd a) - 1))
    let route5 = ((fst a) + 1, ((snd a) + 1))
    let route6 = ((fst a) + 1, ((snd a) - 1))
    let route7 = ((fst a) - 1, ((snd a) - 1))
    let route8 = ((fst a) - 1, ((snd a) + 1))
    let bestRoute = List.filter(fun v -> (dist v b) < (dist a b)) [route1; route2; route3; route4; route5; route6; route7; route8]
    bestRoute

             
/// <summary> Connects pos to shortest candidates. stops when a is equal to target </summary>
/// <param name = a> The posistion where the robot is </param>
/// <param name = b> The position where the robot needs to go </param>
/// <returns> returns all the posible routes from a to b </returns>
let rec routes a b =
    match a with
        a when a = b -> [[b]]
        |_-> 
            List.map (fun v -> List.map (fun i -> a :: i) (routes v b)) (candidates a b) |> List.concat

/// <summary> Filters out the non-shortest routes </summary>
/// <param name = a> The posistion where the robot is </param>
/// <param name = b> The position where the robot needs to go </param>
/// <returns> returns all the shortest posible routes from a to b </returns>
let filter a b= 
    let lengthFinder = List.map (fun v -> List.length v) (routes a b) 
    List.filter (fun v -> List.length v = List.min(lengthFinder)) (routes a b)

printfn "routes: %A" (filter src tgt)


