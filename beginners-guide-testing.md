# [A Beginner’s Guide to Testing: Error Handling Edge Cases](https://www.freecodecamp.org/news/a-beginners-guide-to-testing-implement-these-quick-checks-to-test-your-code-d50027ad5eed/)

When building complex pieces of software, regardless of language, you start to notice a pattern in your testing habits. The same similar-looking issues will arise across different platforms or projects. Regardless of whether you’re building another simple to-do list demo for a talk or architecting a comprehensive back-end for a PaaS startup, the same generic patterns begin to emerge.

There are six cases that should be tested that will shine a light on a surprising number of issues. These are not meant to be comprehensive, or a complete test suite of their own. Rather, they’re an easy-to-remember subset of common testing paradigms that can apply to any language, framework, or environment.

These cases are immediately useful in two aspects of daily coding routines: debugging specific issues as they arise, and in the creation of the testing suite for a code base. They are intended to be generic, abstract forms of testing that will shine a light on some of the most common issues junior developers face.

These will only be useful in a roundabout way in functional programming. Functional programming circumvents many of the simplest types of bugs outlined below. Either way, it’s useful to keep these sort of abstract boundary cases in mind, as they provide a guard rail against bad practices in code.

The six tests are as follows:
1. Zero
2. One
3. Two
4. Two to max-1
5. max
6. max+1

Even though these are boundary cases, their value is in what they represent. While ensuring that your tests cover all functionality of your program, you should keep your tests simple with as a little flair as possible.

-----------------------------------------------------------

## Zero
Zero is used to signify any form of null input, whether that’s undefined, null, an empty array, or simply the actual number 0. Arguably the most common and simple form of bug is referencing a Zero value, and it always bears testing. Simply test a function, endpoint, or upload with a Zero input, and verify that it behaves as expected.

## One
One, like Zero, is the most basic form of the genericized single test. The function gets tested with the first valid, normal input. This is most useful for regression testing. In future iterations of the code, this test will quickly indicate if the program (or process) is operating as expected.

One testing gives you a baseline for success, whether that’s a successful authentication on an admin endpoint, a valid file upload, or a correct array modification.

## Two
Two is not simply about testing array index 2, or whether your algorithm works with 2 inputs. It also encompasses what happens when you run the same code twice.

If someone were to make a DELETE HTTP request twice in a row to the same resource, what happens? If the sort function with a custom comparator gets called twice in a row, does it behave as expected?

Two is an interesting number, because it’s the first time in which valid code that works when called once can show side effects on repeated executions. Take a small change to the functions we’ve tested above.

It comes down to modifications of state, and understanding the behavior of a function. If all we have is the function name then this code behaves precisely as anticipated. You have a variable called 0, you call the function setVarToOne, and then you assert that it’s equal to one.

On first, glance, this behaved exactly as expected. However, testing it with the idea of Two in mind would highlight deeper issues with the code. You’d test it by calling it twice, and asserting that in both cases, mVar is equal to 1.

## Two to max-1
Two to max-1 is the sanity check. It’s very similar to the One test, but there’s a subtle difference. This should be an average use case — not the simplest or most straightforward, or the easiest to read. Just an average use case that perhaps isn’t particularly simple, but that’s fairly common.

## Max
Max is fairly straightforward: it simply tests the limits of your application, especially around defined max constants.

If you have a simple linked list implementation, you might imagine that you have a seemingly infinite number of allowed inserts. In reality, there is an upper limit — whether that’s INT_MAX, the number of file descriptors your OS can have open, or simply the amount of memory or disk space allocated for your program.

Under some circumstances, Max might seem like an impossible test because there is no known max for whatever you’re testing. It’s goal in these cases, however, is of another nature: to stress test your application.

For instance, it’s possible that a certain piece of user-submitted data gets reduced and passed through functions until it reaches a loop you’ve defined. If this data is, say, INT_MAX, it might take a non-negligible amount of time for your code to complete. Worse, it might throw your code into a non-halting state. These can be subtle issues that only arise once your code goes into production, so it’s important to catch them during the testing phase.

## Max+1
Max+1 is a test that is mostly used to verify the standards or rules put in place by the programmer. This involves testing anything to its theoretical limit + epsilon.

This could manifest as an array out of bounds problem, an off by one error, an integer overflow error, or any other sort of problem that happens when you reach the boundaries of your function or program.

If you have a max file upload size of 2mb, try uploading a file that’s 2mb+1b in size. If you have a limit on the number of entries in a user catalog, make sure that the verification is happening both client side and server side.

-----------------------------------------------------------

## Conclusion
As mentioned above, this isn’t a complete picture of what your debugging or testing routines should be. This simply provides a solid, generic baseline that should transcend any specific testing suite or framework.

The tests are commonly seen as boundary or edge cases, but they can rear their ugly head in places that aren’t immediately obvious.

-----------------------------------------------------------

## Source
https://www.freecodecamp.org/news/a-beginners-guide-to-testing-implement-these-quick-checks-to-test-your-code-d50027ad5eed/