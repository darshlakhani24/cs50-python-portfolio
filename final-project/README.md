# BILL SPLITTER PROGRAM
#### Video Demo: https://youtu.be/SUn2Bm7GFvU?si=ZXZzF1dB2DwWZbMV
#### Description: A Python-based bill-splitting program that calculates equal or custom contributions (with optional tips) to ensure the total matches the bill, promoting fairness in shared expenses.

The Bill Splitter is a simple Python-based command-line application I designed to help groups of people fairly divide a bill. It allows users to input a total bill amount, optionally add a tip, and then choose between either equally splitting the bill or inputting custom contributions from each individual. The program calculates and divides the shares and offers a summary in the end.

Idea Origination:

As a boy studying in a residential school, I have built incredibly strong friendships. Living together, studying together, eating together—we do almost everything as a unit. My friends come from diverse backgrounds, with different financial backgrounds. Most times, when we hung out together and it was time to pay, the issue of splitting the bill came up.

In almost all cases, only one person ended up paying the entire bill, simply because they could afford that expense. Although this person never made a fuss and always stepped up generously, I could sense that others felt bad. They wanted to contribute, even if they couldn’t split the amount equally. The situation began to weigh on our interactions and started creating discomfort in an otherwise very close-knit group. We hesitated to hang out together frequently worrying that we're just a burden on others.

To overcome this problem, we started using bill splitting applications online. While searching for an idea for my final project, I became keen on understanding the logic behind these programs and wished to recreate one.  It was this curiosity that led me to choose this project idea: a Bill Splitter that provides equal and custom split options so that everyone can pay what they can without guilt or awkwardness.

Project Structure:

project.py: This is the main script containing all the program logic. It includes the 7 following functions:

get_total_bill(): Prompts the user to input the total bill amount, inclusive of taxes.

get_people(): Gets a list of names from the user for bill splitting.

split_equal(total, people): Equally divides the total bill among all individuals.

split_custom(total, people): Allows the user to input custom contribution amounts for each person. It also validates that the total matches the bill.

tip(amount, tip_percent): Adds a user-defined tip percentage to the total bill.

generate_summary(split, total): Outputs the final summary showing each person's share and the total bill.

main(): Controls the overall flow of the application.

test_project.py: This file includes all test functions for validating core functionalities using pytest. Each function in project.py has a corresponding test_ function:

test_split_equal()

test_tip()

test_generate_summary()

requirements.txt: This file lists pytest as the only external library required to run tests.

Design Decisions:

User-Friendly Prompts: I made a conscious decision to keep prompts and error messages beginner-friendly and polite, ensuring that even someone new to programming or computers could use this application.

Custom Splitting: Adding a custom split was essential. It reflects real-life scenarios where not everyone can contribute equally.

Validation Loops: Many of the input functions are wrapped in while loops to ensure proper data validation. This helps avoid program crashes due to bad input and keeps the user experience smooth.

Fairness Check: If the custom contributions didn’t add up to the total, the program prompts the user to try again. This ensures the bill is always balanced before proceeding.

Tip Handling: Users can optionally add a tip. The final total with the tip is calculated and clearly displayed, ensuring full transparency before bill splitting.

Reflection:

I learned the value of test-driven development. Writing test functions using pytest helped me structure my code better and gave me more confidence that my functions work as expected.

This project has been one of the most personally meaningful experiences I’ve had while learning Python. It’s more than just a technical submission—it’s a tool that grew out of my lived experience. This bill splitter aims to remove those small yet impactful moments of discomfort and promote fairness in a way that everyone feels good about. Although such programs already exist, I feel empowered as this is the first time I used programming to potentially solve a real-life problem myself.

Thank you for reading!
