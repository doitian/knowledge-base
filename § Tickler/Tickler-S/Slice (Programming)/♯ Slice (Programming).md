# Slice (Programming)

#programming

[※ source](https://github.com/nervosnetwork/slice-cheatcheat)

§ Definitions

```			
arr = [1, 2, 3, 4, 5, 6, 7, 8]
```
			
§ Rust
			
``` rust
arr[1..5]  //=> [2, 3, 4, 5]
arr[1..=5] //=> [2, 3, 4, 5, 6]
```

§ Golang

``` go
arr[1:5] //=> [2, 3, 4, 5]
```

§ Python

``` python
arr[1:5]    #=> [2, 3, 4, 5]
arr[1:5:2]  #=> [2, 4]
arr[1:5:3]  #=> [2, 5]
arr[5:1:-1] #=> [6, 5, 4, 3]
arr[2..-1]  #=> [3, 4, 5, 6, 7]
arr[2..-2]  #=> [3, 4, 5, 6]
arr[-5..-1] #=> [4, 5, 6, 7]
arr[5:1:-1] #=> [6, 5, 4, 3]
arr[::-1]   #=> [8, 7, 6, 5, 4, 3, 2, 1]
```

§ Ruby

``` ruby
arr[1, 5]   #=> [2, 3, 4, 5, 6]
arr[2, 5]   #=> [3, 4, 5, 6, 7]
arr[1..5]   #=> [2, 3, 4, 5, 6]
arr[2..5]   #=> [3, 4, 5, 6]
arr[2...5]  #=> [3, 4, 5]
arr[2..-1]  #=> [3, 4, 5, 6, 7, 8]
arr[2..-2]  #=> [3, 4, 5, 6, 7]
arr[-5..-1] #=> [4, 5, 6, 7, 8]
arr[2...-1] #=> [3, 4, 5, 6, 7]
```
			
§ ECMAScript TC39

``` javascript
const obj = { 0: 'a', 1: 'b', 2: 'c', 3: 'd', length: 4 };
```


``` javascript
arr[1:4]   //=> [2, 3, 4]
arr[1:4:2] //=> [2, 4]
obj[1:3]   //=> ['b', 'c']
```