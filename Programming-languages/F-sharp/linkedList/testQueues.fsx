open intQueue
open SafeIntQueue
open Queues

//----------------------intQueueTest----------------------//
printfn "--- 5i1 - intQueueTest---"
let intQueueTests () =
    let q0 = intQueue.emptyQueue
    let emptyTestResult = intQueue.isEmpty q0
    emptyTestResult
    |> printfn "An empty queue is empty: %A"

    let e1 ,e2 ,e3 = 1,2,3
    let q1 = q0 |> intQueue.enqueue e1
                |> intQueue.enqueue e2
                |> intQueue.enqueue e3
    let nonEmptyTestResult = not(intQueue.isEmpty q1)
    nonEmptyTestResult
    |> printfn "A queue with elements is not empty: %A"

    let (e,q2) = intQueue.dequeue q1
    let dequeueTestResult = e = e1
    dequeueTestResult
    |> printfn "First in is first out: %A"

    let allTestResults =
        emptyTestResult &&
        nonEmptyTestResult &&
        dequeueTestResult
    
    allTestResults
    |> printfn "All IntQueue tests passed: %A"
    // Return the test results as a boolean
    allTestResults

let intQueueTestResults = intQueueTests ()
printfn "  "
printfn "  "
//----------------------safeIntQueueTest----------------------//
printfn "---5i2 - safeIntQueueTest---"
let safeIntQueueTests () =
    let q0 = []
    let q1 = [1;2;3]
    printfn "Empty list:   %A" (SafeIntQueue.dequeue q0)
    printfn "nonEmtpylist: %A" (SafeIntQueue.dequeue q1)

let safeIntQueueTestResult = safeIntQueueTests ()
printfn "  "
printfn "  "

//----------------------QueuesTest----------------------//
printfn "---5i3 - queuesTest---"
printfn "int: " //int
let IntQueueTests () =
    let q0 = Queues.emptyQueue
    let emptyTestResult = Queues.isEmpty q0
    emptyTestResult
    |> printfn "An empty queue is empty: %A"

    let e1 ,e2 ,e3 = 1,2,3
    let q1 = q0 |> Queues.enqueue e1
                |> Queues.enqueue e2
                |> Queues.enqueue e3
    let nonEmptyTestResult = not(Queues.isEmpty q1)
    nonEmptyTestResult
    |> printfn "A queue with elements is not empty: %A"

    let (e,q2) = Queues.dequeue q1
    let dequeueTestResult = e = e1
    dequeueTestResult
    |> printfn "First in is first out: %A"

    let allTestResults =
        emptyTestResult &&
        nonEmptyTestResult &&
        dequeueTestResult
    
    allTestResults
    |> printfn "All IntQueue tests passed: %A"
    // Return the test results as a boolean
    allTestResults

let IntQueueTestResults = IntQueueTests ()
printfn "  "

printfn "float: " //floats
let floatQueueTests () =
    let q0 = Queues.emptyQueue
    let emptyTestResult = Queues.isEmpty q0
    emptyTestResult
    |> printfn "An empty queue is empty: %A"

    let e1 ,e2 ,e3 = 1.0,2.0,3.0
    let q1 = q0 |> Queues.enqueue e1
                |> Queues.enqueue e2
                |> Queues.enqueue e3
    let nonEmptyTestResult = not(Queues.isEmpty q1)
    nonEmptyTestResult
    |> printfn "A queue with elements is not empty: %A"

    let (e,q2) = Queues.dequeue q1
    let dequeueTestResult = e = e1
    dequeueTestResult
    |> printfn "First in is first out: %A"

    let allTestResults =
        emptyTestResult &&
        nonEmptyTestResult &&
        dequeueTestResult
    
    allTestResults
    |> printfn "All IntQueue tests passed: %A"
    // Return the test results as a boolean
    allTestResults

let floatQueueTestResults = floatQueueTests ()
printfn "  "

printfn "string: " //strings
let stringQueueTests () =
    let q0 = Queues.emptyQueue
    let emptyTestResult = Queues.isEmpty q0
    emptyTestResult
    |> printfn "An empty queue is empty: %A"

    let e1 ,e2 ,e3 = "Hello","Mr.","Kasper"
    let q1 = q0 |> Queues.enqueue e1
                |> Queues.enqueue e2
                |> Queues.enqueue e3
    let nonEmptyTestResult = not(Queues.isEmpty q1)
    nonEmptyTestResult
    |> printfn "A queue with elements is not empty: %A"

    let (e,q2) = Queues.dequeue q1
    let dequeueTestResult = e = e1
    dequeueTestResult
    |> printfn "First in is first out: %A"

    let allTestResults =
        emptyTestResult &&
        nonEmptyTestResult &&
        dequeueTestResult
    
    allTestResults
    |> printfn "All IntQueue tests passed: %A"
    // Return the test results as a boolean
    allTestResults

let stringQueueTestResults = stringQueueTests ()
printfn "  "