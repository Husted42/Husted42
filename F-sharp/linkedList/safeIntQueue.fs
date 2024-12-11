module SafeIntQueue
type queue = int List
type element = int

///<summary> Creates an empty queue </summary>
///<returs> Returns an empty queue </returs>
let emptyQueue : queue = []

///<summary> Checks if a queue is empty </summary>
///<param name = q> a list of type [int list] </param>
///<returs> Returns true or false </returs>
let isEmpty (q: queue): bool =
    match q with 
        [] -> true
        |_-> false

///<summary> Adds a new elmement to the back of a list </summary>
///<param name = e> a new element </param>
///<param name = q> a list of type [int list] </param>
///<returs> Returns a queue with new element</returs>
let enqueue (e: element) (q: queue) : queue =
    List.rev(e :: List.rev(q))

///<summary> splits first element and the rest of queue </summary>
///<param name = q> a list of type [int list] </param>
///<returs> Returns a tuple of (element option, queue)</returs>
let dequeue (n: queue) =
    match n with
    [] -> (None, [])
    |_-> (Some(List.head(n)), List.tail(n))