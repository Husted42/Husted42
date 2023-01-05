module Queues
type queue<'a> = 'a list
type element<'a> = 'a

///<summary> Creates an empty queue </summary>
///<returs> Returns an empty queue </returs>
let emptyQueue : queue<'a> = []

///<summary> Checks if a queue is empty </summary>
///<param name = q> a list of type ['a list] </param>
///<returs> Returns true or false </returs>
let isEmpty (q: queue<'a>): bool =
    match q with 
        [] -> true
        |_-> false

///<summary> Adds a new elmement to the back of a list </summary>
///<param name = e> a new element </param>
///<param name = q> a list of type ['a list] </param>
///<returs> Returns a queue with new element</returs>
let enqueue (e: element<'a>) (q: queue<'a>) : queue<'a> =
    List.rev(e :: List.rev(q))

///<summary> splits first element and the rest of queue </summary>
///<param name = q> a list of type ['a list] </param>
///<returs> Returns a tuple of (elmement<'a>, queue<'a>)</returs>
let dequeue (q: queue<'a>) = 
    (List.head(q), List.tail(q))

