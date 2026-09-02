module CatList
open DiffList

//Type specification
type 'a catlist =
    | Empty
    | Single of 'a
    | Append of 'a catlist * 'a catlist

//Functions
let nil = Empty

let single (elm:'a) : 'a catlist =
    Single elm

let append (xs : 'a catlist) (ys : 'a catlist) : 'a catlist =
    Append (xs, ys)

let cons (elm : 'a) (xs : 'a catlist) : 'a catlist =
    append (single elm) xs

let snoc (xs : 'a catlist) (elm : 'a) : 'a catlist =
    append xs (single elm)

let fold (cf:('a -> 'a -> 'a),(e:'a)) (f:('b->'a)) (xs:'b catlist) : 'a =
    let rec g xs =
        match xs with
        | Empty -> e
        | Single x -> f x        
        | Append (ys,zs) -> cf (g ys) (g zs)
    g xs

let length (xs : 'a catlist) = fold ((+), 0) (fun _ -> 1) xs
let sum (xs : 'a catlist) = fold ((+), 0) (fun t -> t) xs 

let fromCatList (xs : 'a catlist) : 'a list =
    let rec f t =
        match t with
            Empty -> 
                []
            | Single t -> 
                t :: []
            | Append (x,y) -> 
                f x @ f y
    f xs

let toCatList (xs : 'a list) : 'a catlist =
    let rec f t =
        match t with
            | [] -> Empty
            | x :: t -> cons x (f t)
    f xs

let item (int:int) (xs : 'a catlist) : 'a =
    let rec f int xs =
        match xs with
            Empty -> 
                failwith "Fail: Empty"
            | Single n when int = 0 -> 
                n
            | Append (x, y) -> 
                let l = length x
                if int < l
                then 
                    f int x
                else 
                    f (int - l) y
            |_-> 
                failwith "Fail: Wildcard"
    f int xs

let insert (int:int) (elm:'a) (xs:'a catlist) : 'a catlist =
    let rec f int xs =
        if int = 0 
        then 
            (cons elm xs)
        elif 
            int = length xs 
        then 
            snoc xs elm
        else
            match xs with
                | Append (x, y) ->
                    if int < (length (x)) 
                    then Append (f int (x), (y))
                    else Append (x, f (int-length (x)) y)
                |_-> failwith "fejl"
    f int xs

let delete (int:int) (xs:'a catlist) : 'a catlist =
    let rec f int xs =
        match xs with
            Single elm when int = 0 -> 
                nil
            | Append (x, y) ->
                if int < (length (x)) 
                then Append (f int (x), (y))
                else Append (x, f (int-(length x)) y)
            |_-> 
                failwith "Fail: Wildcard"
    f int xs

// test
let test = 
    let catlistTest = snoc (append(single 2) (single 3) |> append (single 1)) 4
    printfn "catlistTest: %A" catlistTest
    printfn ""
    printfn ""
    printfn "forventet fromCatList: [1; 2; 3; 4]"
    printfn "fromCatList: %A" (fromCatList catlistTest)
    printfn ""
    printfn "forventet toCatList: (Single 1, Append (Single 2, Append (Single 3, Append (Single 4, Empty))))"
    printfn "toCatList:   %A" (toCatList(fromCatList catlistTest))
    printfn ""
    printfn "forventet item: 3"
    printfn "item:        %A" (item 2 catlistTest)
    printfn ""
    printfn "forventet insert: Append (Append (Single 1, Append (Single 2, Append (Single 10, Single 3))), Single 4)"
    printfn "insert:      %A" (insert 2 10 catlistTest)
    printfn ""
    printfn "forventet delete: Append (Append (Single 1, Append (Empty, Single 3)), Single 4)"
    printfn "delete:      %A" (delete 1 catlistTest)
    printfn ""
    printfn "forventet lenght: 3"
    printfn "lenght:      %A" (length catlistTest)
    printfn ""
    printfn "Succses"
test