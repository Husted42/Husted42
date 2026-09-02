module CatList

type 'a catlist =
    | Empty
    | Single of 'a
    | Append of 'a catlist * 'a catlist

val nil : 'a catlist

/// <summary> Take a element of any type and converts it into 'a catlist </summary>
/// <param name = elm> The element that needs to be converted into type: 'a catlist </param>
/// <returns> Returns 'a catlist </returns>
val single : 'a -> 'a catlist

/// <summary> Creates a tuple of type 'a catlist contaning two catlist </summary>
/// <param name = xs> 'a catlist for first coordinate (x) of tuple </param>
/// <param name = ys> 'a catlist for second coordinate (y) of tuple </param>
/// <returns> Returns 'a catlist  </returns>
val append : 'a catlist -> 'a catlist -> 'a catlist

/// <summary> creates a tuple of (single of 'a) * 'a catlist </summary>
/// <param name = elm> The element that is added to the first coordinate (x) </param>
/// <param name = xs > The catlist that is added to the second coordinate (y) </param>
/// <returns> Returns 'a catlist </returns>
val cons : 'a -> 'a catlist -> 'a catlist

/// <summary> Creates new catlist: append('a catalist, single elm) </summary>
/// <param name = xs > The catlist that is added to the first coordinate (x)</param>
/// <param name = elm> The element that is added to the second coordinate (y) </param>
/// <returns> Returns 'a catlist </returns>
val snoc : 'a catlist -> 'a -> 'a catlist

/// <summary> Applies cf to all elemnts in list </summary>
/// <param name = cf > ((The "thing" that is applied), (What Empty is converted to)) </param>
/// <param name = f  > How elements should be treated || if f= (fun _ -> 1) then all element will have value 1 </param>
/// <param name = xs > 'a catlist </param>
/// <returns> Returns a generic element: 'a </returns>
val fold : (('a -> 'a -> 'a) * 'a) -> ('b -> 'a) -> 'b catlist -> 'a

/// <summary> Takes a catlist and converts it to 'a list </summary>
/// <param name = xs > 'a catlist </param>
/// <returns> Returns 'a list'</returns>
val fromCatList : 'a catlist -> 'a list

/// <summary> Takes a 'a list and converts it to 'a catlist </summary>
/// <param name = xs > 'a catlist </param>
/// <returns> Returns 'a list'</returns>    
val toCatList : 'a list -> 'a catlist

/// <summary> Returns the value of a given index </summary>
/// <param name = int > The index that item returns </param>
/// <param name = xs > 'a catlist </param>
/// <returns> Returns an element of type: 'a</returns>
val item : int -> 'a catlist -> 'a

/// <summary> Adds a new element to a given index </summary>
/// <param name = int > the index where element is inserted </param>
/// <param name = elm > the element that gets added to catlist </param>
/// <returns> Returns 'a catlist'</returns>
val insert : int -> 'a -> 'a catlist -> 'a catlist

/// <summary> deletes an element to a given index </summary>
/// <param name = int > the index where element is deleted </param>
/// <returns> Returns 'a catlist'</returns>
val delete : int -> 'a catlist -> 'a catlist
