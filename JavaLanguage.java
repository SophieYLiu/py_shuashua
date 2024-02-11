/*
Order of execution of the initialization blocks: static, then instances, public, then private
1. constructor
2. static methods
3. non-static methods
4. standard methods (toStirng, equals, hashcode etc)
5. getter, setter
*/
/**********************************************************/

// reverse an arraylist
Collections.reverse(lst);

// copy array
int[] arr = {23, 43, 55, 12}
int[] copied = Arrays.copyOf(arr, arr.length); // full copy
int[] copied = Arrays.copyOfRange(arr, 0, arr.length); // full copy
arr.clone(); // ?
System.arraycopy(a, 0, b, 0 ,3) // 3 is the len

// copy list
list.subList(1,3)
/**********************************************************/
// check escape quote. Eg "Alexandra ""Alex""" -> Alexandra "Alex"
str.charAt(i) == '\"' 

/**********************************************************/
// flatmap
List<Interval> schedules = schedules.stream()
									.flatMap(List:stream)
									.collect(Collectors.toList());

/**********************************************************/
// PQ with custom comparator
PriorityQueue<Interval> pq = new PriorityQueue<>(new comparator<>(){
	public int compare(Interval a, Interval b) {
		if (a.start == b.start) {
			return a.end - b.end;
		}
		return a.start - b.start;
	}
})

/**********************************************************/
// CONVERSION

// int to char
int num = 2;
char w = (char) (num + '0') // w = '2'
char w = (char) num // w maybe '.' or '\u002'?

// object to String
String.valueOf(xx) // xx could be char array

// Array to ArrayList
List<Integer> list = Arrays.asList(arr)

// ArrayList to int[]
int[] arr = list.stream().mapToInt(i -> i).toArray();

// ArrayList to Integer[]
Integer[] arr = list.toArray(new Integer[list.size()]); // toArray结果是object[]

/**********************************************************/
// String and String Builder
String[] parts = Arrays.stream(path.split('/'))
						.filter(e -> e.trim().length > 0)
						.toArray(String[]::new)

StringBuilder sb = new StringBuilder();
sb.setLength(0); // clear the object
sb.delete(1, 2); // delete 1th pos
sb.append(num); // even if num is integer, it can be appended to it and becomes a string later (so no need to convert it to char)


// LinkedList
addLast(i), removeLast()

// ArrayDeque


// TreeMap
treemap.ceilingKey(i) // get the key that 1. 刚好比他大，或者自己（if exists），或者null
treemap.floorKey(i) // get the key that 1. 刚好比他小，或者自己（if exists），或者null



/**********************************************************/
// MSCS
Optional<Intent> intent;
intent.isPresent() ? intent.get().getName() : null;
-> intent.map(Intent :: getName).orElse(null);

/**********************************************************/
TimeUnit.MILLISECONDS.convert(10L, TimeUnit.MINUTE); // convert 10 min to milliseconds

