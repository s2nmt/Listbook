#!/usr/bin/env python3
import json
import re
from pathlib import Path

# ===== Điền nội dung sách tại đây =====
stories = [
    {
        "name": "The Talking Dog",
        "bookNote": (
            "A man sees a sign: 'Talking Dog for Sale.' He rings the bell and the owner tells him the dog is in the "
            "backyard. The man asks the dog, 'Can you talk?' 'Yep,' the dog replies. 'I worked for the CIA, traveling "
            "the world. Now I'm retired.' Amazed, the man asks the owner how much. The owner says, 'Ten dollars.' "
            "'Why so cheap?' The owner replies, 'He's a liar. He never did any of that.'"
        ),
    },
    {
        "name": "The Genie and the Three Wishes",
        "bookNote": (
            "A man finds a lamp and rubs it, releasing a genie. The genie grants him three wishes. The man wishes for a "
            "million dollars, and poof, a million dollars appear. He wishes for a luxury car, and poof, a car appears. "
            "For his final wish, he asks to be irresistible to women. Poof, he's turned into a box of chocolates."
        ),
    },
    {
        "name": "The Parrot with a Foul Mouth",
        "bookNote": (
            "A woman buys a parrot that previously lived in a bar. The parrot constantly swears. She tries to teach it "
            "polite words, but it keeps swearing. In frustration, she puts the parrot in the freezer for a few minutes. "
            "When she takes it out, the parrot apologizes and asks, 'What did the chicken do?'"
        ),
    },
    {
        "name": "The Doctor's Diagnosis",
        "bookNote": (
            "A man goes to the doctor and says, 'Doctor, I think I'm a moth.' The doctor replies, 'You need a "
            "psychiatrist, not a doctor.' The man says, 'I know, but your light was on.'"
        ),
    },
    {
        "name": "The Lawyer and the Farmer",
        "bookNote": (
            "A lawyer and a farmer are sitting next to each other on a plane. The lawyer asks if the farmer wants to "
            "play a game. The farmer declines, wanting to sleep. The lawyer insists, offering to pay the farmer $5 for "
            "every question he can't answer, while the farmer only has to pay $1. The lawyer asks, 'What's the distance "
            "between the Earth and the Moon?' The farmer hands over $1. The farmer asks, 'What goes up a hill with three "
            "legs and comes down with four?' The lawyer is stumped, gives the farmer $5, and asks, 'What is it?' The "
            "farmer hands over $1 and goes back to sleep."
        ),
    },
    {
        "name": "The Forgetful Professor",
        "bookNote": (
            "A professor was known for being absent-minded. One day, his wife said, 'Don't forget we're moving today.' "
            "He promised to remember. Later, he returned to the old house and found it empty. Realizing his mistake, he "
            "sat on the porch. A child passing by asked, 'Are you moving in?' The professor replied, 'No, I think I "
            "already moved out.'"
        ),
    },
    {
        "name": "The Clever Dog",
        "bookNote": (
            "A man walked into a bar with his dog. The bartender said, 'No dogs allowed.' The man replied, 'But my dog "
            "can talk!' Skeptical, the bartender asked, 'What's on top of a house?' The dog barked, 'Roof!' The "
            "bartender, unimpressed, said, 'Get out!' As they left, the dog turned to his owner and said, 'Should I have "
            "said ceiling?'"
        ),
    },
    {
        "name": "The Broken Umbrella",
        "bookNote": (
            "It was raining heavily when Jane left the house. She grabbed her umbrella and rushed outside. As soon as she "
            "opened it, the wind turned it inside out! She tried to fix it, but the wind was too strong. Finally, she "
            "gave up and walked in the rain, holding the broken umbrella like a modern art sculpture."
        ),
    },
    {
        "name": "The Talking Parrot",
        "bookNote": (
            "A man bought a parrot that was supposed to speak. After weeks of silence, he returned to the pet shop. The "
            "shopkeeper asked, 'Did you buy a mirror for the parrot?' The man said no. 'That's the problem,' said the "
            "shopkeeper. 'Parrots love to look at themselves and talk!' The man bought a mirror, and the parrot started "
            "talking immediately."
        ),
    },
    {
        "name": "The Pink Socks",
        "bookNote": (
            "John opened the package and found a pair of bright pink socks! Confused, he checked his order and realized "
            "he had clicked the wrong item. Mary laughed when she saw the socks, and they both had a good laugh. John "
            "decided to wear them anyway, and they became his lucky socks."
        ),
    },
    {
        "name": "The Password Predicament",
        "bookNote": (
            "Mark set his new computer password as 'incorrect.' That way, if he forgot it, the system would prompt him, "
            "'Your password is incorrect.' It worked like a charm until his colleague tried to log in and exclaimed, "
            "'Your password is incorrect?' Mark grinned, 'Exactly!'"
        ),
    },
    {
        "name": "The Time-Traveling Typo",
        "bookNote": (
            "Emma sent an email to her boss, intending to write, 'I'll have the report to you by tomorrow.' However, "
            "autocorrect changed 'tomorrow' to 'yesterday.' Her boss replied, 'Impressive! Can you also predict next "
            "week's lottery numbers?'"
        ),
    },
    {
        "name": "The Silent Treatment",
        "bookNote": (
            "After a minor argument, Jake and his wife decided to give each other the silent treatment. That evening, Jake "
            "needed his wife to wake him up at 6 AM for an early flight. Not wanting to break the silence, he wrote on a "
            "piece of paper, 'Please wake me at 6 AM.' The next morning, he woke up at 9 AM and found a note beside him: "
            "'It's 6 AM. Wake up.'"
        ),
    },
    {
        "name": "The Autocorrect Apology",
        "bookNote": (
            "Tom texted his friend, 'I'm sorry for the incontinence.' He meant 'inconvenience,' but autocorrect had other "
            "plans. His friend replied, 'No worries, but maybe see a doctor about that.'"
        ),
    },
    {
        "name": "The Wi-Fi Password",
        "bookNote": (
            "At a café, a customer asked for the Wi-Fi password. The barista replied, 'You need to buy a coffee first.' "
            "The customer bought a coffee and asked again. The barista said, 'You need to buy a coffee first—all "
            "lowercase, no spaces.'"
        ),
    },
    {
        "name": "The Diet Dilemma",
        "bookNote": (
            "Sarah decided to eat healthier and told her friend, 'I'm on a seafood diet.' Her friend replied, 'I thought "
            "you were avoiding seafood.' Sarah laughed, 'No, I see food, and I eat it.'"
        ),
    },
    {
        "name": "The Job Interview",
        "bookNote": (
            "During a job interview, the interviewer asked, 'What's your greatest weakness?' The candidate replied, "
            "'Honesty.' The interviewer said, 'I don't think honesty is a weakness.' The candidate responded, 'I don't "
            "care what you think.'"
        ),
    },
    {
        "name": "The Library Lament",
        "bookNote": (
            "A man walked into a library and asked the librarian, 'Where are the books on paranoia?' She whispered, "
            "'They're right behind you.'"
        ),
    },
    {
        "name": "The Coffee Conundrum",
        "bookNote": (
            "Every morning, Lisa ordered a 'grande' coffee at her local café. One day, feeling adventurous, she asked for "
            "a 'venti.' The barista smiled and said, 'That's Italian for twenty. Are you sure you want twenty ounces of "
            "caffeine?' Lisa laughed and replied, 'I guess I'll stick with my grande—I don't need to be that awake!'"
        ),
    },
    {
        "name": "The Elevator Small Talk Escape",
        "bookNote": (
            "John stepped into the elevator, dreading the inevitable small talk. As the doors closed, his colleague, "
            "Sarah, asked, 'How was your weekend?' John, thinking quickly, replied, 'I spent it learning ventriloquism.' "
            "He then threw his voice, making it seem like someone else in the elevator said, 'Please, no small talk.' "
            "Sarah looked around, puzzled, and John enjoyed a quiet ride up."
        ),
    },
    {
        "name": "The Lost Phone",
        "bookNote": (
            "Sarah spent ten minutes searching for her phone, calling it from her landline to hear it ring. She checked "
            "under the couch, in the kitchen, and even in the refrigerator. Finally, she realized she was holding it in "
            "her hand the entire time. She had been using it as a flashlight to search for it."
        ),
    },
    {
        "name": "The Unintended Text",
        "bookNote": (
            "Mark sent a text complaining about his boss to his colleague. However, he accidentally sent it directly to "
            "his boss. Fortunately, his boss had a sense of humor and replied, 'I think so too!'"
        ),
    },
    {
        "name": "The Coffee Spill",
        "bookNote": (
            "Lisa rushed to a morning meeting and decided to bring a cup of coffee. When she entered the meeting room, "
            "she tripped and spilled coffee all over her boss's shirt. The room fell silent until her boss laughed and "
            "said, 'I needed some caffeine too!'"
        ),
    },
    {
        "name": "The Auto-Correct Mishap",
        "bookNote": (
            "Tom texted his girlfriend, wanting to write 'I miss you,' but autocorrect changed it to 'I mess you.' His "
            "girlfriend replied, 'Yes, you always mess me up!'"
        ),
    },
    {
        "name": "The Wrong Number",
        "bookNote": (
            "A man received a text message that said, 'I'm at the restaurant. Where are you?' He replied, 'I think you "
            "have the wrong number.' The person texted back, 'Are you sure? This is my husband's number.' The man "
            "replied, 'I'm very sure. I'm a single woman.'"
        ),
    },
    {
        "name": "The Parking Ticket",
        "bookNote": (
            "A man parked his car and saw a parking meter that said '2 hours free parking.' He was thrilled and went "
            "shopping. When he returned, he found a parking ticket on his windshield. Confused, he read the meter again. "
            "It actually said '2 hours free parking—if you pay for 3 hours.'"
        ),
    },
    {
        "name": "The Restaurant Order",
        "bookNote": (
            "A man ordered a pizza and asked for extra cheese. When the pizza arrived, he was disappointed to see it had "
            "no cheese at all. He called the restaurant to complain. The manager said, 'You asked for extra cheese, so we "
            "gave you extra—on the side.'"
        ),
    },
    {
        "name": "The Gym Membership",
        "bookNote": (
            "A man signed up for a gym membership, excited to get in shape. On his first day, he walked in and saw a sign "
            "that said 'Free pizza for new members!' He thought, 'This is the best gym ever!' Then he realized he was in "
            "the wrong building—it was a pizza place next door."
        ),
    },
    {
        "name": "The Birthday Cake",
        "bookNote": (
            "A woman ordered a birthday cake that said 'Happy 30th Birthday!' When she picked it up, the cake said 'Happy "
            "80th Birthday!' She called the bakery to complain. The baker said, 'I'm so sorry! I must have misread the "
            "order. But look on the bright side—you look great for 80!'"
        ),
    },
    {
        "name": "The Weather Forecast",
        "bookNote": (
            "The weather forecast said it would be sunny all day. A man left his umbrella at home and went to work. "
            "Halfway there, it started pouring rain. He called the weather service to complain. They said, 'We forecast "
            "the weather, not control it!'"
        ),
    },
    {
        "name": "The Missing Keys",
        "bookNote": (
            "A man spent an hour searching for his car keys. He looked in his pockets, under the couch, and even in the "
            "refrigerator. Finally, his wife asked, 'Did you check your hand?' He looked down and saw the keys in his "
            "hand the entire time. He had been holding them while searching for them."
        ),
    },
    {
        "name": "The Alarm Clock",
        "bookNote": (
            "A man set his alarm clock for 6 AM, but it didn't go off. He woke up at 8 AM and was late for work. When he "
            "checked the alarm clock, he realized he had set it for 6 PM instead of 6 AM. He thought, 'Well, at least I'll "
            "be on time for dinner.'"
        ),
    },
    {
        "name": "The Shopping List",
        "bookNote": (
            "A woman wrote a shopping list: milk, eggs, bread, and butter. When she got to the store, she realized she had "
            "forgotten the list at home. She called her husband and asked him to read it to her. He said, 'I can't find it. "
            "Where did you leave it?' She replied, 'On the kitchen counter, next to the milk, eggs, bread, and butter.'"
        ),
    },
    {
        "name": "The GPS Navigation",
        "bookNote": (
            "A man was following GPS directions to a restaurant. The GPS told him to turn left, but he turned right by "
            "mistake. The GPS said, 'Recalculating route.' He turned around and went back. The GPS said, 'Recalculating "
            "route.' He thought, 'This GPS is as confused as I am!'"
        ),
    },
    {
        "name": "The Restaurant Bill",
        "bookNote": (
            "A couple went to a restaurant and ordered dinner. When the bill came, the man was shocked to see it was $200. "
            "He asked the waiter, 'Is this correct?' The waiter replied, 'Yes, sir. You ordered the most expensive items "
            "on the menu.' The man said, 'I thought the prices were in cents, not dollars!'"
        ),
    },
    {
        "name": "The Movie Ticket",
        "bookNote": (
            "A man bought a movie ticket and went to see the film. Halfway through, he realized he was in the wrong "
            "theater. He was watching a romantic comedy, but he had bought a ticket for an action movie. He thought, 'Well, "
            "at least this movie is better than the one I paid for!'"
        ),
    },
    {
        "name": "The Dry Cleaner",
        "bookNote": (
            "A man took his suit to the dry cleaner and asked them to remove a stain. When he picked it up, the stain was "
            "gone, but there was a hole where the stain had been. He asked, 'What happened?' The dry cleaner said, 'We had "
            "to cut it out. The stain was too stubborn.'"
        ),
    },
    {
        "name": "The Haircut",
        "bookNote": (
            "A man went to a barber and asked for a trim. The barber cut his hair too short. The man said, 'I asked for a "
            "trim, not a buzz cut!' The barber replied, 'I'm sorry, but your hair was so long, I got carried away. But look "
            "on the bright side—you'll save money on shampoo!'"
        ),
    },
    {
        "name": "The Taxi Driver",
        "bookNote": (
            "A man got into a taxi and told the driver his destination. The driver started driving in the opposite "
            "direction. The man said, 'You're going the wrong way!' The driver replied, 'I know, but I'm new to this city. "
            "I'm just exploring!'"
        ),
    },
    {
        "name": "The Elevator",
        "bookNote": (
            "A man got into an elevator and pressed the button for the 10th floor. The elevator went up to the 15th floor "
            "instead. He pressed the button again, and it went down to the 5th floor. He thought, 'This elevator has a mind "
            "of its own!'"
        ),
    },
    {
        "name": "The Hotel Room",
        "bookNote": (
            "A man checked into a hotel and was given room 101. When he opened the door, he saw another person already in "
            "the room. He said, 'I'm sorry, I think there's been a mistake.' The other person said, 'No mistake. This is my "
            "room. You must have the wrong number.' The man checked his key card—it said room 110."
        ),
    },
    {
        "name": "The Package Delivery",
        "bookNote": (
            "A man was expecting a package delivery. The delivery person left a note saying, 'Package delivered to your "
            "neighbor.' The man went to his neighbor's house to get the package. His neighbor said, 'I don't have your "
            "package. I think the delivery person got the wrong address.'"
        ),
    },
    {
        "name": "The ATM Machine",
        "bookNote": (
            "A man went to an ATM to withdraw money. He inserted his card and entered his PIN. The machine said, 'Insufficient "
            "funds.' He thought, 'That's strange. I just deposited money yesterday.' Then he realized he was using his "
            "credit card instead of his debit card."
        ),
    },
    {
        "name": "The Coffee Shop",
        "bookNote": (
            "A man ordered a large coffee at a coffee shop. The barista gave him a small coffee instead. He said, 'I ordered "
            "a large coffee.' The barista replied, 'I'm sorry, but we're out of large cups. This is the largest we have.' "
            "The man thought, 'Then why do you have a large option on the menu?'"
        ),
    },
    {
        "name": "The Parking Space",
        "bookNote": (
            "A man found a parking space and started to park his car. Another car pulled in from the other side and took the "
            "space. The man said, 'I was here first!' The other driver said, 'I don't see your name on it!' The man "
            "replied, 'I don't see yours either!'"
        ),
    },
    {
        "name": "The Grocery Store",
        "bookNote": (
            "A man went to the grocery store to buy milk. He walked up and down the aisles but couldn't find it. He asked a "
            "store employee, 'Where is the milk?' The employee said, 'It's in the dairy section, aisle 3.' The man said, "
            "'I'm in aisle 3, and I don't see it.' The employee said, 'That's because you're in the frozen food section.'"
        ),
    },
    {
        "name": "The Doctor's Appointment",
        "bookNote": (
            "A man made a doctor's appointment for 2 PM. He arrived at 2:30 PM and was told he was late. He said, 'I'm only "
            "30 minutes late.' The receptionist said, 'Yes, but your appointment was for 2 PM, not 2:30 PM.' The man "
            "replied, 'I know, but I thought doctors were always running late, so I thought I'd be on time if I came late!'"
        ),
    },
    {
        "name": "The Restaurant Reservation",
        "bookNote": (
            "A couple made a restaurant reservation for 7 PM. When they arrived, the restaurant was closed. They called the "
            "restaurant and asked why it was closed. The manager said, 'We're closed on Mondays.' The couple said, 'But "
            "today is Tuesday!' The manager replied, 'I know, but we're still closed.'"
        ),
    },
    {
        "name": "The Movie Theater",
        "bookNote": (
            "A man went to a movie theater and bought a ticket. When he entered the theater, he saw that the movie had "
            "already started. He asked an usher, 'When did the movie start?' The usher said, 'About 20 minutes ago.' The "
            "man said, 'But the ticket says 7 PM!' The usher replied, 'Yes, but the movie started at 6:40 PM.'"
        ),
    },
    {
        "name": "The Gas Station",
        "bookNote": (
            "A man pulled into a gas station and asked the attendant to fill up his car. The attendant said, 'I'm sorry, but "
            "we're out of gas.' The man said, 'But you're a gas station!' The attendant replied, 'I know, but we ran out "
            "this morning. The delivery truck is late.'"
        ),
    },
]
# =======================================

output_dir = Path("stories")
output_dir.mkdir(parents=True, exist_ok=True)

def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "story"

for index, story in enumerate(stories, start=1):
    base_slug = slugify(story["name"])
    filename = output_dir / f"{index:02d}-{base_slug}.txt"
    payload = {
        "name": story["name"],
        "bookNote": story["bookNote"],
        "bookSections": [],
        "chapters": [],
    }
    with filename.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Saved JSON to {filename.resolve()}")
