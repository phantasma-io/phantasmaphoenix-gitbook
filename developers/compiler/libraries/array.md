# Array

{% hint style="info" %}
The Array library exposes methods to manipulate arrays. It is also possible to manipulate arrays directly via TOMB array variables.
{% endhint %}

| Method                                               | Return type | Description                                                          |
| ---------------------------------------------------- | ----------- | -------------------------------------------------------------------- |
| Array.get(array:Any, index:Number)                   | Generic<0>  | Returns the element of an array at the given index.                  |
| Array.set(array:Any, index:Number, value:Generic<0>) | None        | Set the element of an array at the given index with the given value. |
| Array.remove(array:Any, index:Number)                | None        | Removes the element of an array at the given index.                  |
| Array.clear(array:Any)                               | None        | Clears all the Array entries.                                        |
| Array.length(array:Any)                              | Number      | Returns the number of elements in the Array.                         |
