#!/usr/bin/env python3
import json
import re
from pathlib import Path

# ===== Điền nội dung sách tại đây =====
stories = [
    {
        "name": "Elevator Small Talk Escape",
        "bookNote": (
            "Ellie boarded the elevator planning to ride in silence, but a stranger enthusiastically asked about her "
            "weekend plans. She panicked, blurted out that she was training for a competitive napping league, and "
            "immediately regretted everything. The stranger applauded, requested tickets, and the elevator stopped "
            "three floors early. Ellie took the stairs the rest of the week to avoid a rematch."
        ),
    },
    {
        "name": "Decaf Disaster Day",
        "bookNote": (
            "Marcus proudly announced he had switched to decaf to become a calmer version of himself. Thirty minutes "
            "later he realized he had brewed regular coffee, powered through two presentations, reorganized the supply "
            "closet, and apologized to the office plant for speaking too loudly. He now labels every mug with sticky "
            "notes like an overcaffeinated librarian guarding secrets."
        ),
    },
    {
        "name": "Laundry Basket Plot Twist",
        "bookNote": (
            "Priya decided to fold laundry like a responsible adult, but the basket swallowed every matching sock she "
            "thought she owned. She interrogated her washing machine, checked under the couch, and briefly suspected "
            "her goldfish. Eventually she paired two socks that only kind of matched and declared mismatched confidence "
            "the new trend for the entire apartment building."
        ),
    },
    {
        "name": "Conference Call Cameo",
        "bookNote": (
            "During a very serious quarterly meeting, Jonah carefully muted himself, nodded thoughtfully, and tried to "
            "silently eat potato chips. His cat chose that moment to leap onto the keyboard, unmuting him and "
            "broadcasting the crunchiest bite in company history. Leadership applauded his commitment to transparency "
            "and asked for the brand of chips in the chat."
        ),
    },
    {
        "name": "Candle Scent Detective",
        "bookNote": (
            "Rena hosted a cozy game night and promised a prize to whoever guessed the candle scent. Guesses ranged from "
            "‘fresh optimism’ to ‘new shoe memories.’ When the label revealed vanilla bean, everyone gasped dramatically "
            "and accused Rena of emotional misdirection. She handed out cookies, declared everyone correct, and retired "
            "from candle-based contests forever."
        ),
    },
    {
        "name": "Inbox Archaeologist",
        "bookNote": (
            "Dev opened his email to find a message he had sent himself six months ago titled IMPORTANT. Inside he had "
            "written a single sentence: “Do not forget to breathe.” He spent ten minutes trying to decode the hidden "
            "meaning, decided past Dev was either a philosopher or exhausted, and marked it complete with a triumphant "
            "sigh."
        ),
    },
    {
        "name": "Midnight Chef Symphony",
        "bookNote": (
            "Lara attempted a quiet midnight grilled cheese, confident she could cook without waking her roommates. "
            "Instead she triggered the smoke alarm, serenaded the building with fan noises, and waved a dish towel like "
            "a conductor embracing chaotic jazz. The sandwich survived, slightly toasted and very proud of its dramatic "
            "debut."
        ),
    },
    {
        "name": "Backpack Time Capsule",
        "bookNote": (
            "Andre cleaned his backpack for the first time since winter and discovered a fossilized granola bar, seven "
            "pens without caps, and a heartfelt note reminding him to buy batteries. He framed the note as an artifact "
            "from a wiser era and kept the granola bar as emergency motivation for future excavations."
        ),
    },
    {
        "name": "Grocery Cart Diplomacy",
        "bookNote": (
            "Sonia promised herself she would only buy essentials, then steered her cart directly into the snack aisle "
            "for what she called morale research. She negotiated with herself out loud, compromised on three flavors of "
            "chips instead of five, and left a voice memo titled “do not shop hungry” that she will heroically ignore "
            "next week."
        ),
    },
    {
        "name": "Weather App Betrayal",
        "bookNote": (
            "Hector trusted his weather app, wore sunglasses, and packed sunscreen for the commute. Halfway to work, "
            "rain erupted like a dramatic plot twist. He took shelter under a cafe awning, ordered hot chocolate, and "
            "wrote a strongly worded letter to the clouds. The sun reappeared five minutes later, looking smug."
        ),
    },
    {
        "name": "Dance Floor Daydream",
        "bookNote": (
            "Mia practiced her best dance moves in the hallway while waiting for laundry to finish. The elevator doors "
            "opened unexpectedly, revealing a delivery driver applauding her interpretive spin. She bowed, collected her "
            "package, and now refers to the hallway as Studio M whenever neighbors walk by."
        ),
    },
    {
        "name": "Plant Parent Hotline",
        "bookNote": (
            "Theo worried his fern looked bored, so he read motivational quotes to it every morning. One day he spotted a "
            "new leaf and immediately texted six friends to announce Fernando’s growth spurt. The group chat responded "
            "with confetti emojis and unsolicited fertilizer tips, turning Theo into the proudest plant parent on the "
            "block."
        ),
    },
    {
        "name": "Charging Cable Maze",
        "bookNote": (
            "Harper opened her drawer of random cables to find the single charger that fit her aging tablet. Instead she "
            "found a collection of mystery connectors, two headphones from 2011, and a dramatic sense of betrayal. She "
            "labeled the drawer “tech archaeology” and now charges everything in the kitchen like a renegade."
        ),
    },
    {
        "name": "Playlist Weather Report",
        "bookNote": (
            "Gus lets his shuffled playlist determine the day’s mood. One morning he got three power ballads in a row and "
            "announced a 90 percent chance of dramatic hair flips. By lunchtime the playlist switched to acoustic lull "
            "abies, and he declared a nap advisory that nobody obeyed."
        ),
    },
    {
        "name": "Sticky Note Philosopher",
        "bookNote": (
            "Lana covers her monitor with motivational sticky notes like “remember snacks” and “breathe more than coffee.” "
            "When she ran out of space, she stuck one on her reusable water bottle saying “hydrate the thoughts.” Now she "
            "walks into meetings armed with pastel wisdom and a notebook labeled Profound Scheduling."
        ),
    },
    {
        "name": "Window Meteorologist",
        "bookNote": (
            "Colin insists on forecasting weather by touching his apartment window. He declared Tuesday “brisk but "
            "optimistic,” dressed in layers, and stepped outside into a humid wall of summer. He blamed the lying glass, "
            "went back in for shorts, and started drafting an apology letter to his ceiling fan."
        ),
    },
    {
        "name": "Pen Borrowing Economy",
        "bookNote": (
            "Nadia lends pens with tiny contracts attached, yet still never gets them back. She started naming each pen "
            "before lending it out, hoping sentimental guilt would help. Now everyone at the office proudly claims to be "
            "co-parenting pens named Gerald, Dot, and Sparkle. Nadia has accepted her new role as stationary diplomat."
        ),
    },
    {
        "name": "Squeaky Chair Serenade",
        "bookNote": (
            "Omar’s office chair squeaks a high note every time he leans forward, so he times important comments with the "
            "sound for maximum dramatic effect. His teammates think he has a custom soundtrack. The chair recently added "
            "a mysterious bass note, and now meetings feel suspiciously like rehearsals."
        ),
    },
    {
        "name": "Remote Control Detective",
        "bookNote": (
            "Lena spent fifteen minutes searching for the TV remote, only to discover it balanced on top of the fridge "
            "next to a half-eaten brownie. She held a brief courtroom session accusing her future self of sabotage. The "
            "remote was acquitted, and the brownie was sentenced to immediate consumption."
        ),
    },
    {
        "name": "Commute Comedy Routine",
        "bookNote": (
            "Ben narrates his walk to work like a travel show host. He critiques puddles, compliments dogs on their "
            "fashion choices, and interviews pigeons about city infrastructure. One morning a tourist applauded and asked "
            "for the channel. Ben winked, promised new episodes daily, and kept pretending the sidewalk was a red carpet."
        ),
    },
    {
        "name": "Library Whisper Workout",
        "bookNote": (
            "Jade tried whispering during a video call at the library, forgetting that whispering while wearing "
            "headphones sounds suspiciously like dramatic ASMR. Her teammates muted themselves to laugh while she "
            "gestured wildly to assure them she was not being chased by book ghosts. She now schedules calls only near "
            "the potted ficus, her official soundproof booth."
        ),
    },
    {
        "name": "Dramatic Thermostat Summit",
        "bookNote": (
            "Roommates Ezra and Quinn hold weekly diplomatic summits over thermostat settings. Ezra arrives with charts, "
            "Quinn arrives with blankets. After hours of negotiation they settle on a number neither can remember and end "
            "up adjusting it again before breakfast. They now refer to the thermostat as The Negotiator."
        ),
    },
    {
        "name": "Gala Of Leftovers",
        "bookNote": (
            "Tori hosted a leftover night, plated everything on fancy dishes, and gave dramatic speeches about reheated "
            "lasagna. Her microwave beeped like a trumpet fanfare. By dessert, which consisted of half a brownie and a "
            "single grape, everyone agreed it was the most glamorous refrigerator clean-out in neighborhood history."
        ),
    },
    {
        "name": "Notebook Overachiever",
        "bookNote": (
            "Caleb buys a new notebook every time he has a fresh idea. Page one always gets filled with bullet points, "
            "page two with doodles, and the remaining pages remain pristine monuments to potential. His friends staged an "
            "intervention, gifting him a notebook titled “Finish Me.” Caleb is considering it."
        ),
    },
    {
        "name": "Giant Tote Bag Mystery",
        "bookNote": (
            "Serena carries a tote bag that could legally qualify as a tiny apartment. Inside you will find snacks, three "
            "umbrellas, a novel, and occasionally a stray sock. She insists everything has a purpose, though she once "
            "pulled out a whisk during a staff meeting and simply said, “emergency morale tool.”"
        ),
    },
    {
        "name": "Calendar Time Traveler",
        "bookNote": (
            "Hugh forgot to move last year’s calendar off the wall and only realized it when June mysteriously repeated "
            "itself. He shrugged, declared bonus summer, and treated himself to popsicles. Eventually a neighbor pointed "
            "out the mistake, and Hugh promised to embrace the actual timeline with minimal confusion."
        ),
    },
    {
        "name": "Gaming Night Referee",
        "bookNote": (
            "During board game night, Mei brought a referee whistle to keep her friends honest. She issued playful yellow "
            "cards for excessive bragging and one dramatic red card when someone hid extra game pieces. The whistle has "
            "since become part of every gathering, even quiet movie nights, just in case popcorn negotiations get heated."
        ),
    },
    {
        "name": "DIY Haircut Chronicles",
        "bookNote": (
            "Garrett decided to trim his own hair, watched two tutorials, and felt unstoppable until the mirror reflected "
            "a lopsided masterpiece. He styled the longer side like a swooping cape and joined his video call with heroic "
            "lighting. Coworkers applauded his bravery, and Garrett promised the sequel would involve professional "
            "backup."
        ),
    },
    {
        "name": "Closet Light Show",
        "bookNote": (
            "Every time Nina opens her closet, motion-sensor lights flicker dramatically, making her feel like a celebrity "
            "entering stage left. She has started narrating her outfit choices in a British accent for added flair. The "
            "cat watches from the doorway, clearly judging but secretly invested in the wardrobe plotline."
        ),
    },
    {
        "name": "Mismatched Mug Meeting",
        "bookNote": (
            "Oli collects mugs with obscure slogans. During a morning meeting his camera revealed one that read “Official "
            "Pancake Inspector,” prompting the team to send him inspection forms. He obliged, reviewing everyone’s "
            "breakfasts with serious eye squints and imaginary clipboards. Productivity was questionable, morale was "
            "excellent."
        ),
    },
    {
        "name": "Doorway Blank Mind",
        "bookNote": (
            "Tessa walked into the kitchen with purpose, forgot why, and stood very still like a statue gathering wisdom. "
            "Her roommate asked if she was buffering. Tessa finally remembered she wanted cereal, grabbed a spoon, and "
            "celebrated the small victory with a triumphant dance beside the fridge."
        ),
    },
    {
        "name": "Unexpected Parade Rehearsal",
        "bookNote": (
            "Vic practiced playing the kazoo for an upcoming charity parade, unaware that the open window turned the "
            "entire street into his audience. Neighbors peeked out, clapped along, and someone shouted for an encore. Vic "
            "took a bow, promised wardrobe upgrades, and now refers to his living room as the rehearsal hall."
        ),
    },
    {
        "name": "Supermarket Compliment Patrol",
        "bookNote": (
            "Riley wandered the grocery store complimenting strangers’ produce choices. She told one shopper their "
            "watermelon looked heroic and congratulated another on brave bell peppers. The compliments started a chain "
            "reaction, and soon half the aisle was praising each other’s carts. The store manager called it Tuesday."
        ),
    },
    {
        "name": "Wi-Fi Password Poet",
        "bookNote": (
            "Mina renamed the home Wi-Fi to “PleaseWaterThePlants” so roommates would remember chores. Instead, delivery "
            "drivers left sticky notes saying the network name inspired them. She has since rotated passwords like “Fold "
            "Laundry Maybe” and “TextYourGrandma,” turning tech support into motivational messaging."
        ),
    },
    {
        "name": "Desk Drawer Mystery",
        "bookNote": (
            "Jon keeps finding glitter in his desk drawer despite never owning glitter. He suspects a crafty ghost or "
            "possibly the enthusiastic intern who loves scrapbooks. Rather than investigate, he simply signs every email "
            "with a sparkly flourish to match the ambiance."
        ),
    },
    {
        "name": "Puddle Jumping Commute",
        "bookNote": (
            "When the sidewalk flooded, Kara decided to hop over puddles like an action hero. She landed with dramatic "
            "flourishes, narrated her own slow-motion replay, and earned applause from a passing dog walker. The final "
            "puddle soaked her completely, but she bowed anyway and declared victory on behalf of playful mornings."
        ),
    },
    {
        "name": "Late Night Philosophy Club",
        "bookNote": (
            "Oscar swore he would sleep early, then discovered a documentary about bees at midnight. He whispered "
            "questions to the screen, took furious notes, and texted friends philosophical thoughts about honey "
            "democracy. No one responded until morning, when they gently reminded him that sleep is also important."
        ),
    },
    {
        "name": "Paper Towel Stage Show",
        "bookNote": (
            "Sasha replaced the paper towel roll and accidentally pulled the entire sheet like a magician revealing a "
            "banner. Instead of rewinding it, she staged a miniature theater curtain for her countertop fruit bowl. Guests "
            "now applaud before taking oranges."
        ),
    },
    {
        "name": "Phone Flashlight Expedition",
        "bookNote": (
            "Ian used his phone flashlight to search for his phone, wandering around the apartment narrating the quest. "
            "After five minutes he noticed his reflection holding the glowing device like a lantern. He bowed to himself, "
            "declared the expedition successful, and wrote “remember pockets exist” on a sticky note."
        ),
    },
    {
        "name": "Closet Concert Series",
        "bookNote": (
            "Becca sings full concerts while picking outfits, using hangers as microphones. One morning she finished an "
            "encore to find her roommate sitting cross-legged on the floor holding up a concert rating sign. Becca "
            "accepted the imaginary trophy and promised backstage passes after laundry day."
        ),
    },
    {
        "name": "Notebook Margin Doodles",
        "bookNote": (
            "During a long webinar, Felix doodled extravagant dragons in the margins of his notes. When the facilitator "
            "asked him to share key takeaways, he held up a dragon labeled “burn out notifications.” The chat exploded "
            "with laughter, and Felix earned the unofficial title of morale illustrator."
        ),
    },
    {
        "name": "Microwave Countdown Drama",
        "bookNote": (
            "Jules treats the microwave countdown like a suspense thriller, refusing to let it beep. She sprints across "
            "the kitchen to stop it at exactly one second, pumping her fists in victory. Her smartwatch thinks she is "
            "doing interval training and keeps congratulating her for daily heroics."
        ),
    },
    {
        "name": "Doorbell Costume Party",
        "bookNote": (
            "Whenever the doorbell rings, Marco throws on the first costume he finds from his theater days. Delivery "
            "drivers never know if a pirate, astronaut, or Victorian poet will sign for the package. Reviews consistently "
            "mention prompt payment and outstanding dedication to bit comedy."
        ),
    },
    {
        "name": "Morning Mirror Pep Talk",
        "bookNote": (
            "Skye gives herself a pep talk every morning using a tiny travel mirror. One day she dropped it, caught it "
            "with a dramatic flourish, and cheered for her own reflexes. The pep talk turned into a spontaneous dance "
            "party with toothpaste foam providing stage fog."
        ),
    },
    {
        "name": "Desk Plant News Network",
        "bookNote": (
            "Luca updates his desk plant on daily headlines to keep it in the loop. He reports on weather, coffee "
            "shortages, and the thrilling saga of his inbox. The plant recently sprouted a new leaf, which Luca interprets "
            "as a request for sports coverage."
        ),
    },
    {
        "name": "Forgotten Lunch Adventure",
        "bookNote": (
            "Dana packed lunch, left it by the door, and realized the mistake only after bragging about homemade pesto at "
            "work. She transformed the oversight into a scavenger hunt, trading snacks with coworkers until she built an "
            "impressive sampler platter. The pesto enjoyed a nice day off at home."
        ),
    },
    {
        "name": "Closet Light Applause",
        "bookNote": (
            "Whenever Rowan flips on the closet light, the motion sensor beams like a spotlight. Rowan bows, narrates the "
            "outfit selection, and thanks the invisible audience. Laundry day now feels like a matinee performance with "
            "sock encores."
        ),
    },
    {
        "name": "Overprepared Picnic Trio",
        "bookNote": (
            "Three friends planned a simple picnic, then each arrived with enough snacks to feed a marching band. They "
            "arranged everything into courses, invented fancy menu names, and invited curious squirrels as guest judges. "
            "The squirrels stole a cracker, which everyone considered a glowing review."
        ),
    },
    {
        "name": "Staircase Motivational Speech",
        "bookNote": (
            "While climbing six flights, Arman gave himself a motivational speech out loud, complete with inspirational "
            "quotes and dramatic pauses. Halfway up he realized a neighbor was trailing behind, silently cheering. They "
            "finished the stairs together like a victorious marathon team."
        ),
    },
    {
        "name": "DIY Award Ceremony",
        "bookNote": (
            "Lily created a weekly award show for everyday accomplishments. She gives herself trophies made of cereal "
            "boxes for feats like remembering laundry or resisting online sales. Acceptance speeches happen in the mirror, "
            "and the applause button is a wooden spoon tapping a bowl."
        ),
    },
    {
        "name": "Neighborhood Compliment Walk",
        "bookNote": (
            "Sam takes evening walks dedicated to complimenting anything he sees. He congratulates porch pumpkins on their "
            "posture, applauds tidy hedges, and tells lampposts they are glowing examples of dedication. Neighbors now "
            "time their gardening to coincide with his cheerful commentary."
        ),
    },
    {
        "name": "Impromptu Kitchen Parade",
        "bookNote": (
            "Poppy turned cooking dinner into a parade by marching around the kitchen banging wooden spoons on pots. "
            "Roommates joined with spatulas and reusable containers as makeshift drums. The pasta boiled over during the "
            "grand finale, which everyone applauded as an avant-garde steam effect."
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
