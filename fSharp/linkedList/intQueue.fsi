module intQueue
type queue = int List
type element = int

// the empty queue
val emptyQueue: queue

// add an element at the end of a queue
val enqueue: element -> queue -> queue
// remove and return the element at the front of a queue
// precondition: input queue is not empty
val dequeue: queue -> (element * queue)

// check if a queue is empty
val isEmpty: queue -> bool