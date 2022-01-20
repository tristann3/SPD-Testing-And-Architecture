# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1

Here I used Trace Backwards in the flask error on the broswer to identify that line 79 had a Type Error. By command clicking PizzaTopping, we can see the variable is called topping_type instead of topping.

After that there was a werkzeug error. Again I can use Trace Back to identify that on line 84 in app.py there is a routing error. instead of redirecting to '/', flask uses "url_for" (which is imported at the top of the file) to redirect to a specific file specified in the templates folder, similar to line 96 in app.py

After the routing issue, we now are redirected back to the homepage after we submit a pizza, but there are no pizzas being shown here. We expect a list of pizza orders to show up after a user submits them. by looking at the pizza data I saw the vaiable names of the pizza_size and order_name had to be changed. Then I realized the checkboxes weren't being fetched correctly, I googled how to fetch all checked boxes in a flask checkbox list, and added 'getlist' instead of 'get'


## Exercise 2

[[Your answer goes here!]]

## Exercise 3

[[Your answer goes here!]]
