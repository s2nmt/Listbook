#!/usr/bin/env python3
import json
import re
from pathlib import Path

# ===== Điền nội dung sách tại đây =====
stories = [
    {
        "name": "The Talking Dog",
        "bookNote": {
            "en": (
                "A man sees a sign: 'Talking Dog for Sale.' He rings the bell and the owner tells him the dog is in the "
                "backyard. The man asks the dog, 'Can you talk?' 'Yep,' the dog replies. 'I worked for the CIA, traveling "
                "the world. Now I'm retired.' Amazed, the man asks the owner how much. The owner says, 'Ten dollars.' "
                "'Why so cheap?' The owner replies, 'He's a liar. He never did any of that.'"
            ),
            "vi": (
                "Một người đàn ông thấy biển hiệu: 'Chó biết nói bán.' Anh ta bấm chuông và chủ nhà nói con chó đang ở "
                "sân sau. Người đàn ông hỏi con chó, 'Bạn có biết nói không?' 'Có chứ,' con chó trả lời. 'Tôi đã làm việc cho CIA, đi khắp "
                "thế giới. Giờ tôi đã nghỉ hưu.' Ngạc nhiên, người đàn ông hỏi chủ nhà giá bao nhiêu. Chủ nhà nói, 'Mười đô la.' "
                "'Sao rẻ thế?' Chủ nhà trả lời, 'Nó là kẻ nói dối. Nó chưa bao giờ làm những việc đó.'"
            ),
        },
    },
    {
        "name": "The Genie and the Three Wishes",
        "bookNote": {
            "en": (
                "A man finds a lamp and rubs it, releasing a genie. The genie grants him three wishes. The man wishes for a "
                "million dollars, and poof, a million dollars appear. He wishes for a luxury car, and poof, a car appears. "
                "For his final wish, he asks to be irresistible to women. Poof, he's turned into a box of chocolates."
            ),
            "vi": (
                "Một người đàn ông tìm thấy một chiếc đèn và chà xát nó, giải phóng một vị thần. Vị thần ban cho anh ta ba điều ước. Người đàn ông ước có một "
                "triệu đô la, và poof, một triệu đô la xuất hiện. Anh ta ước có một chiếc xe sang trọng, và poof, một chiếc xe xuất hiện. "
                "Với điều ước cuối cùng, anh ta xin được trở nên không thể cưỡng lại với phụ nữ. Poof, anh ta biến thành một hộp sô cô la."
            ),
        },
    },
    {
        "name": "The Parrot with a Foul Mouth",
        "bookNote": {
            "en": (
                "A woman buys a parrot that previously lived in a bar. The parrot constantly swears. She tries to teach it "
                "polite words, but it keeps swearing. In frustration, she puts the parrot in the freezer for a few minutes. "
                "When she takes it out, the parrot apologizes and asks, 'What did the chicken do?'"
            ),
            "vi": (
                "Một phụ nữ mua một con vẹt từng sống trong quán bar. Con vẹt liên tục chửi thề. Cô cố dạy nó "
                "những từ lịch sự, nhưng nó vẫn tiếp tục chửi thề. Trong sự bực bội, cô đặt con vẹt vào tủ đông vài phút. "
                "Khi cô lấy nó ra, con vẹt xin lỗi và hỏi, 'Con gà đã làm gì vậy?'"
            ),
        },
    },
    {
        "name": "The Doctor's Diagnosis",
        "bookNote": {
            "en": (
                "A man goes to the doctor and says, 'Doctor, I think I'm a moth.' The doctor replies, 'You need a "
                "psychiatrist, not a doctor.' The man says, 'I know, but your light was on.'"
            ),
            "vi": (
                "Một người đàn ông đến gặp bác sĩ và nói, 'Bác sĩ, tôi nghĩ tôi là một con bướm đêm.' Bác sĩ trả lời, 'Anh cần một "
                "bác sĩ tâm thần, không phải bác sĩ thường.' Người đàn ông nói, 'Tôi biết, nhưng đèn của ông đang bật.'"
            ),
        },
    },
    {
        "name": "The Lawyer and the Farmer",
        "bookNote": {
            "en": (
                "A lawyer and a farmer are sitting next to each other on a plane. The lawyer asks if the farmer wants to "
                "play a game. The farmer declines, wanting to sleep. The lawyer insists, offering to pay the farmer $5 for "
                "every question he can't answer, while the farmer only has to pay $1. The lawyer asks, 'What's the distance "
                "between the Earth and the Moon?' The farmer hands over $1. The farmer asks, 'What goes up a hill with three "
                "legs and comes down with four?' The lawyer is stumped, gives the farmer $5, and asks, 'What is it?' The "
                "farmer hands over $1 and goes back to sleep."
            ),
            "vi": (
                "Một luật sư và một nông dân ngồi cạnh nhau trên máy bay. Luật sư hỏi nông dân có muốn "
                "chơi một trò chơi không. Nông dân từ chối, muốn ngủ. Luật sư nài nỉ, đề nghị trả nông dân 5 đô cho "
                "mỗi câu hỏi anh ta không trả lời được, trong khi nông dân chỉ phải trả 1 đô. Luật sư hỏi, 'Khoảng cách "
                "giữa Trái Đất và Mặt Trăng là bao nhiêu?' Nông dân đưa 1 đô. Nông dân hỏi, 'Cái gì lên đồi với ba "
                "chân và xuống với bốn chân?' Luật sư bí, đưa nông dân 5 đô, và hỏi, 'Đó là gì?' "
                "Nông dân đưa 1 đô và quay lại ngủ."
            ),
        },
    },
    {
        "name": "The Forgetful Professor",
        "bookNote": {
            "en": (
                "A professor was known for being absent-minded. One day, his wife said, 'Don't forget we're moving today.' "
                "He promised to remember. Later, he returned to the old house and found it empty. Realizing his mistake, he "
                "sat on the porch. A child passing by asked, 'Are you moving in?' The professor replied, 'No, I think I "
                "already moved out.'"
            ),
            "vi": (
                "Một giáo sư nổi tiếng vì hay quên. Một ngày, vợ ông nói, 'Đừng quên hôm nay chúng ta chuyển nhà.' "
                "Ông hứa sẽ nhớ. Sau đó, ông trở về ngôi nhà cũ và thấy nó trống rỗng. Nhận ra sai lầm, ông "
                "ngồi trên hiên nhà. Một đứa trẻ đi ngang hỏi, 'Ông đang chuyển đến à?' Giáo sư trả lời, 'Không, tôi nghĩ tôi "
                "đã chuyển đi rồi.'"
            ),
        },
    },
    {
        "name": "The Clever Dog",
        "bookNote": {
            "en": (
                "A man walked into a bar with his dog. The bartender said, 'No dogs allowed.' The man replied, 'But my dog "
                "can talk!' Skeptical, the bartender asked, 'What's on top of a house?' The dog barked, 'Roof!' The "
                "bartender, unimpressed, said, 'Get out!' As they left, the dog turned to his owner and said, 'Should I have "
                "said ceiling?'"
            ),
            "vi": (
                "Một người đàn ông bước vào quán bar với con chó của mình. Người phục vụ nói, 'Không cho chó vào.' Người đàn ông trả lời, 'Nhưng con chó của tôi "
                "biết nói!' Nghi ngờ, người phục vụ hỏi, 'Cái gì ở trên nóc nhà?' Con chó sủa, 'Mái nhà!' "
                "Người phục vụ, không ấn tượng, nói, 'Ra ngoài!' Khi họ rời đi, con chó quay lại chủ và nói, 'Tôi có nên "
                "nói trần nhà không?'"
            ),
        },
    },
    {
        "name": "The Broken Umbrella",
        "bookNote": {
            "en": (
                "It was raining heavily when Jane left the house. She grabbed her umbrella and rushed outside. As soon as she "
                "opened it, the wind turned it inside out! She tried to fix it, but the wind was too strong. Finally, she "
                "gave up and walked in the rain, holding the broken umbrella like a modern art sculpture."
            ),
            "vi": (
                "Trời mưa to khi Jane rời khỏi nhà. Cô cầm ô và vội vã ra ngoài. Ngay khi cô "
                "mở nó ra, gió làm nó lộn ngược! Cô cố sửa nó, nhưng gió quá mạnh. Cuối cùng, cô "
                "bỏ cuộc và đi trong mưa, cầm chiếc ô hỏng như một tác phẩm điêu khắc nghệ thuật hiện đại."
            ),
        },
    },
    {
        "name": "The Talking Parrot",
        "bookNote": {
            "en": (
                "A man bought a parrot that was supposed to speak. After weeks of silence, he returned to the pet shop. The "
                "shopkeeper asked, 'Did you buy a mirror for the parrot?' The man said no. 'That's the problem,' said the "
                "shopkeeper. 'Parrots love to look at themselves and talk!' The man bought a mirror, and the parrot started "
                "talking immediately."
            ),
            "vi": (
                "Một người đàn ông mua một con vẹt được cho là biết nói. Sau nhiều tuần im lặng, anh ta trở lại cửa hàng thú cưng. "
                "Chủ cửa hàng hỏi, 'Anh có mua gương cho con vẹt chưa?' Người đàn ông nói chưa. 'Đó là vấn đề,' chủ cửa hàng nói. "
                "'Vẹt thích nhìn mình trong gương và nói chuyện!' Người đàn ông mua một chiếc gương, và con vẹt bắt đầu "
                "nói chuyện ngay lập tức."
            ),
        },
    },
    {
        "name": "The Pink Socks",
        "bookNote": {
            "en": (
                "John opened the package and found a pair of bright pink socks! Confused, he checked his order and realized "
                "he had clicked the wrong item. Mary laughed when she saw the socks, and they both had a good laugh. John "
                "decided to wear them anyway, and they became his lucky socks."
            ),
            "vi": (
                "John mở gói hàng và tìm thấy một đôi tất màu hồng rực rỡ! Bối rối, anh kiểm tra đơn hàng và nhận ra "
                "anh đã nhấp nhầm mục. Mary cười khi cô thấy đôi tất, và cả hai đều cười vui vẻ. John "
                "quyết định vẫn mang chúng, và chúng trở thành đôi tất may mắn của anh."
            ),
        },
    },
    {
        "name": "The Password Predicament",
        "bookNote": {
            "en": (
                "Mark set his new computer password as 'incorrect.' That way, if he forgot it, the system would prompt him, "
                "'Your password is incorrect.' It worked like a charm until his colleague tried to log in and exclaimed, "
                "'Your password is incorrect?' Mark grinned, 'Exactly!'"
            ),
            "vi": (
                "Mark đặt mật khẩu máy tính mới của mình là 'sai.' Bằng cách đó, nếu anh quên, hệ thống sẽ nhắc anh, "
                "'Mật khẩu của bạn không đúng.' Nó hoạt động hoàn hảo cho đến khi đồng nghiệp của anh cố đăng nhập và thốt lên, "
                "'Mật khẩu của bạn không đúng?' Mark cười toe toét, 'Chính xác!'"
            ),
        },
    },
    {
        "name": "The Time-Traveling Typo",
        "bookNote": {
            "en": (
                "Emma sent an email to her boss, intending to write, 'I'll have the report to you by tomorrow.' However, "
                "autocorrect changed 'tomorrow' to 'yesterday.' Her boss replied, 'Impressive! Can you also predict next "
                "week's lottery numbers?'"
            ),
            "vi": (
                "Emma gửi email cho sếp, định viết, 'Tôi sẽ gửi báo cáo cho anh vào ngày mai.' Tuy nhiên, "
                "tự động sửa đã đổi 'ngày mai' thành 'hôm qua.' Sếp của cô trả lời, 'Ấn tượng! Cô cũng có thể dự đoán "
                "số xổ số tuần tới không?'"
            ),
        },
    },
    {
        "name": "The Silent Treatment",
        "bookNote": {
            "en": (
                "After a minor argument, Jake and his wife decided to give each other the silent treatment. That evening, Jake "
                "needed his wife to wake him up at 6 AM for an early flight. Not wanting to break the silence, he wrote on a "
                "piece of paper, 'Please wake me at 6 AM.' The next morning, he woke up at 9 AM and found a note beside him: "
                "'It's 6 AM. Wake up.'"
            ),
            "vi": (
                "Sau một cuộc cãi vã nhỏ, Jake và vợ quyết định im lặng với nhau. Tối hôm đó, Jake "
                "cần vợ đánh thức anh dậy lúc 6 giờ sáng cho chuyến bay sớm. Không muốn phá vỡ sự im lặng, anh viết trên một "
                "mảnh giấy, 'Làm ơn đánh thức tôi lúc 6 giờ sáng.' Sáng hôm sau, anh thức dậy lúc 9 giờ sáng và tìm thấy một mảnh giấy bên cạnh: "
                "'Bây giờ là 6 giờ sáng. Thức dậy đi.'"
            ),
        },
    },
    {
        "name": "The Autocorrect Apology",
        "bookNote": {
            "en": (
                "Tom texted his friend, 'I'm sorry for the incontinence.' He meant 'inconvenience,' but autocorrect had other "
                "plans. His friend replied, 'No worries, but maybe see a doctor about that.'"
            ),
            "vi": (
                "Tom nhắn tin cho bạn, 'Tôi xin lỗi vì sự không kiềm chế.' Anh muốn nói 'bất tiện,' nhưng tự động sửa có "
                "kế hoạch khác. Bạn của anh trả lời, 'Không sao, nhưng có lẽ nên đi khám bác sĩ về vấn đề đó.'"
            ),
        },
    },
    {
        "name": "The Wi-Fi Password",
        "bookNote": {
            "en": (
                "At a café, a customer asked for the Wi-Fi password. The barista replied, 'You need to buy a coffee first.' "
                "The customer bought a coffee and asked again. The barista said, 'You need to buy a coffee first—all "
                "lowercase, no spaces.'"
            ),
            "vi": (
                "Ở một quán cà phê, một khách hàng hỏi mật khẩu Wi-Fi. Người phục vụ trả lời, 'Bạn cần mua cà phê trước.' "
                "Khách hàng mua cà phê và hỏi lại. Người phục vụ nói, 'Bạn cần mua cà phê trước—tất cả "
                "chữ thường, không có khoảng trống.'"
            ),
        },
    },
    {
        "name": "The Diet Dilemma",
        "bookNote": {
            "en": (
                "Sarah decided to eat healthier and told her friend, 'I'm on a seafood diet.' Her friend replied, 'I thought "
                "you were avoiding seafood.' Sarah laughed, 'No, I see food, and I eat it.'"
            ),
            "vi": (
                "Sarah quyết định ăn uống lành mạnh hơn và nói với bạn, 'Tôi đang ăn kiêng hải sản.' Bạn của cô trả lời, 'Tôi nghĩ "
                "bạn đang tránh hải sản.' Sarah cười, 'Không, tôi thấy đồ ăn, và tôi ăn nó.'"
            ),
        },
    },
    {
        "name": "The Job Interview",
        "bookNote": {
            "en": (
                "During a job interview, the interviewer asked, 'What's your greatest weakness?' The candidate replied, "
                "'Honesty.' The interviewer said, 'I don't think honesty is a weakness.' The candidate responded, 'I don't "
                "care what you think.'"
            ),
            "vi": (
                "Trong một cuộc phỏng vấn xin việc, người phỏng vấn hỏi, 'Điểm yếu lớn nhất của bạn là gì?' Ứng viên trả lời, "
                "'Trung thực.' Người phỏng vấn nói, 'Tôi không nghĩ trung thực là điểm yếu.' Ứng viên trả lời, 'Tôi không "
                "quan tâm bạn nghĩ gì.'"
            ),
        },
    },
    {
        "name": "The Smart Refrigerator",
        "bookNote": {
            "en": (
                "A man bought a smart refrigerator that could talk. One day, he opened it and the fridge said, 'You're out of "
                "milk.' The man was impressed and went to buy milk. When he returned, the fridge said, 'You're out of eggs.' "
                "The man went shopping again. After the third trip, the man asked, 'How do you know what I need?' The fridge "
                "replied, 'I've been watching you through your phone camera.'"
            ),
            "vi": (
                "Một người đàn ông mua một chiếc tủ lạnh thông minh có thể nói chuyện. Một ngày, anh mở nó ra và tủ lạnh nói, 'Bạn hết "
                "sữa rồi.' Người đàn ông ấn tượng và đi mua sữa. Khi anh trở về, tủ lạnh nói, 'Bạn hết trứng rồi.' "
                "Người đàn ông lại đi mua sắm. Sau chuyến đi thứ ba, người đàn ông hỏi, 'Làm sao bạn biết tôi cần gì?' Tủ lạnh "
                "trả lời, 'Tôi đã theo dõi bạn qua camera điện thoại của bạn.'"
            ),
        },
    },
    {
        "name": "The Coffee Conundrum",
        "bookNote": {
            "en": (
                "Every morning, Lisa ordered a 'grande' coffee at her local café. One day, feeling adventurous, she asked for "
                "a 'venti.' The barista smiled and said, 'That's Italian for twenty. Are you sure you want twenty ounces of "
                "caffeine?' Lisa laughed and replied, 'I guess I'll stick with my grande—I don't need to be that awake!'"
            ),
            "vi": (
                "Mỗi sáng, Lisa gọi một ly cà phê 'grande' tại quán cà phê địa phương. Một ngày, cảm thấy phiêu lưu, cô hỏi "
                "một ly 'venti.' Người phục vụ cười và nói, 'Đó là tiếng Ý nghĩa là hai mươi. Bạn có chắc muốn hai mươi ounce "
                "caffeine không?' Lisa cười và trả lời, 'Tôi nghĩ tôi sẽ giữ ly grande của mình—tôi không cần tỉnh táo đến thế!'"
            ),
        },
    },
    {
        "name": "The Elevator Small Talk Escape",
        "bookNote": {
            "en": (
                "John stepped into the elevator, dreading the inevitable small talk. As the doors closed, his colleague, "
                "Sarah, asked, 'How was your weekend?' John, thinking quickly, replied, 'I spent it learning ventriloquism.' "
                "He then threw his voice, making it seem like someone else in the elevator said, 'Please, no small talk.' "
                "Sarah looked around, puzzled, and John enjoyed a quiet ride up."
            ),
            "vi": (
                "John bước vào thang máy, lo sợ cuộc trò chuyện nhỏ không thể tránh khỏi. Khi cửa đóng lại, đồng nghiệp của anh, "
                "Sarah, hỏi, 'Cuối tuần của bạn thế nào?' John, suy nghĩ nhanh, trả lời, 'Tôi dành nó để học thuật nói tiếng bụng.' "
                "Sau đó anh ném giọng nói, làm như có người khác trong thang máy nói, 'Làm ơn, không nói chuyện nhỏ.' "
                "Sarah nhìn xung quanh, bối rối, và John tận hưởng một chuyến đi yên tĩnh lên."
            ),
        },
    },
    {
        "name": "The Lost Phone",
        "bookNote": {
            "en": (
                "Sarah spent ten minutes searching for her phone, calling it from her landline to hear it ring. She checked "
                "under the couch, in the kitchen, and even in the refrigerator. Finally, she realized she was holding it in "
                "her hand the entire time. She had been using it as a flashlight to search for it."
            ),
            "vi": (
                "Sarah dành mười phút tìm kiếm điện thoại, gọi nó từ điện thoại cố định để nghe nó đổ chuông. Cô kiểm tra "
                "dưới ghế sofa, trong bếp, và thậm chí trong tủ lạnh. Cuối cùng, cô nhận ra cô đang cầm nó trong "
                "tay suốt thời gian. Cô đã dùng nó như đèn pin để tìm kiếm nó."
            ),
        },
    },
    {
        "name": "The Unintended Text",
        "bookNote": {
            "en": (
                "Mark sent a text complaining about his boss to his colleague. However, he accidentally sent it directly to "
                "his boss. Fortunately, his boss had a sense of humor and replied, 'I think so too!'"
            ),
            "vi": (
                "Mark gửi tin nhắn phàn nàn về sếp của mình cho đồng nghiệp. Tuy nhiên, anh vô tình gửi trực tiếp cho "
                "sếp của mình. May mắn thay, sếp của anh có khiếu hài hước và trả lời, 'Tôi cũng nghĩ vậy!'"
            ),
        },
    },
    {
        "name": "The Coffee Spill",
        "bookNote": {
            "en": (
                "Lisa rushed to a morning meeting and decided to bring a cup of coffee. When she entered the meeting room, "
                "she tripped and spilled coffee all over her boss's shirt. The room fell silent until her boss laughed and "
                "said, 'I needed some caffeine too!'"
            ),
            "vi": (
                "Lisa vội vã đến cuộc họp buổi sáng và quyết định mang một cốc cà phê. Khi cô bước vào phòng họp, "
                "cô vấp ngã và đổ cà phê khắp áo sơ mi của sếp. Căn phòng im lặng cho đến khi sếp của cô cười và "
                "nói, 'Tôi cũng cần một chút caffeine!'"
            ),
        },
    },
    {
        "name": "The Auto-Correct Mishap",
        "bookNote": {
            "en": (
                "Tom texted his girlfriend, wanting to write 'I miss you,' but autocorrect changed it to 'I mess you.' His "
                "girlfriend replied, 'Yes, you always mess me up!'"
            ),
            "vi": (
                "Tom nhắn tin cho bạn gái, muốn viết 'Anh nhớ em,' nhưng tự động sửa đã đổi thành 'Anh làm rối em.' "
                "Bạn gái của anh trả lời, 'Đúng, anh luôn làm rối em!'"
            ),
        },
    },
    {
        "name": "The Wrong Number",
        "bookNote": {
            "en": (
                "A man received a text message that said, 'I'm at the restaurant. Where are you?' He replied, 'I think you "
                "have the wrong number.' The person texted back, 'Are you sure? This is my husband's number.' The man "
                "replied, 'I'm very sure. I'm a single woman.'"
            ),
            "vi": (
                "Một người đàn ông nhận được tin nhắn nói, 'Tôi đang ở nhà hàng. Anh ở đâu?' Anh trả lời, 'Tôi nghĩ bạn "
                "nhầm số.' Người đó nhắn lại, 'Bạn có chắc không? Đây là số của chồng tôi.' Người đàn ông "
                "trả lời, 'Tôi rất chắc. Tôi là một phụ nữ độc thân.'"
            ),
        },
    },
    {
        "name": "The Parking Ticket",
        "bookNote": {
            "en": (
                "A man parked his car and saw a parking meter that said '2 hours free parking.' He was thrilled and went "
                "shopping. When he returned, he found a parking ticket on his windshield. Confused, he read the meter again. "
                "It actually said '2 hours free parking—if you pay for 3 hours.'"
            ),
            "vi": (
                "Một người đàn ông đỗ xe và thấy một đồng hồ đỗ xe nói 'Đỗ xe miễn phí 2 giờ.' Anh vui mừng và đi "
                "mua sắm. Khi anh trở lại, anh tìm thấy một vé phạt đỗ xe trên kính chắn gió. Bối rối, anh đọc lại đồng hồ. "
                "Nó thực sự nói 'Đỗ xe miễn phí 2 giờ—nếu bạn trả cho 3 giờ.'"
            ),
        },
    },
    {
        "name": "The Restaurant Order",
        "bookNote": {
            "en": (
                "A man ordered a pizza and asked for extra cheese. When the pizza arrived, he was disappointed to see it had "
                "no cheese at all. He called the restaurant to complain. The manager said, 'You asked for extra cheese, so we "
                "gave you extra—on the side.'"
            ),
            "vi": (
                "Một người đàn ông đặt pizza và yêu cầu thêm phô mai. Khi pizza đến, anh thất vọng khi thấy nó "
                "không có phô mai nào cả. Anh gọi nhà hàng để phàn nàn. Người quản lý nói, 'Bạn yêu cầu thêm phô mai, vì vậy chúng tôi "
                "đã cho thêm—ở bên cạnh.'"
            ),
        },
    },
    {
        "name": "The Gym Membership",
        "bookNote": {
            "en": (
                "A man signed up for a gym membership, excited to get in shape. On his first day, he walked in and saw a sign "
                "that said 'Free pizza for new members!' He thought, 'This is the best gym ever!' Then he realized he was in "
                "the wrong building—it was a pizza place next door."
            ),
            "vi": (
                "Một người đàn ông đăng ký thành viên phòng gym, hào hứng để có dáng. Vào ngày đầu tiên, anh bước vào và thấy một biển hiệu "
                "nói 'Pizza miễn phí cho thành viên mới!' Anh nghĩ, 'Đây là phòng gym tuyệt nhất từ trước đến nay!' Sau đó anh nhận ra anh đang ở "
                "nhầm tòa nhà—đó là một quán pizza bên cạnh."
            ),
        },
    },
    {
        "name": "The Birthday Cake",
        "bookNote": {
            "en": (
                "A woman ordered a birthday cake that said 'Happy 30th Birthday!' When she picked it up, the cake said 'Happy "
                "80th Birthday!' She called the bakery to complain. The baker said, 'I'm so sorry! I must have misread the "
                "order. But look on the bright side—you look great for 80!'"
            ),
            "vi": (
                "Một phụ nữ đặt một chiếc bánh sinh nhật nói 'Chúc mừng sinh nhật lần thứ 30!' Khi cô nhận nó, chiếc bánh nói 'Chúc mừng "
                "sinh nhật lần thứ 80!' Cô gọi tiệm bánh để phàn nàn. Người thợ làm bánh nói, 'Tôi rất xin lỗi! Tôi chắc đã đọc nhầm "
                "đơn hàng. Nhưng nhìn mặt tích cực—bạn trông tuyệt vời cho 80 tuổi!'"
            ),
        },
    },
    {
        "name": "The Weather Forecast",
        "bookNote": {
            "en": (
                "The weather forecast said it would be sunny all day. A man left his umbrella at home and went to work. "
                "Halfway there, it started pouring rain. He called the weather service to complain. They said, 'We forecast "
                "the weather, not control it!'"
            ),
            "vi": (
                "Dự báo thời tiết nói sẽ nắng cả ngày. Một người đàn ông để ô ở nhà và đi làm. "
                "Nửa đường, trời bắt đầu mưa như trút. Anh gọi dịch vụ thời tiết để phàn nàn. Họ nói, 'Chúng tôi dự báo "
                "thời tiết, không điều khiển nó!'"
            ),
        },
    },
    {
        "name": "The Missing Keys",
        "bookNote": {
            "en": (
                "A man spent an hour searching for his car keys. He looked in his pockets, under the couch, and even in the "
                "refrigerator. Finally, his wife asked, 'Did you check your hand?' He looked down and saw the keys in his "
                "hand the entire time. He had been holding them while searching for them."
            ),
            "vi": (
                "Một người đàn ông dành một giờ tìm kiếm chìa khóa xe. Anh tìm trong túi, dưới ghế sofa, và thậm chí trong "
                "tủ lạnh. Cuối cùng, vợ anh hỏi, 'Anh đã kiểm tra tay của mình chưa?' Anh nhìn xuống và thấy chìa khóa trong "
                "tay suốt thời gian. Anh đã cầm chúng trong khi tìm kiếm chúng."
            ),
        },
    },
    {
        "name": "The Alarm Clock",
        "bookNote": {
            "en": (
                "A man set his alarm clock for 6 AM, but it didn't go off. He woke up at 8 AM and was late for work. When he "
                "checked the alarm clock, he realized he had set it for 6 PM instead of 6 AM. He thought, 'Well, at least I'll "
                "be on time for dinner.'"
            ),
            "vi": (
                "Một người đàn ông đặt đồng hồ báo thức lúc 6 giờ sáng, nhưng nó không kêu. Anh thức dậy lúc 8 giờ sáng và muộn làm việc. Khi anh "
                "kiểm tra đồng hồ báo thức, anh nhận ra anh đã đặt nó lúc 6 giờ chiều thay vì 6 giờ sáng. Anh nghĩ, 'Ồ, ít nhất tôi sẽ "
                "đúng giờ cho bữa tối.'"
            ),
        },
    },
    {
        "name": "The Shopping List",
        "bookNote": {
            "en": (
                "A woman wrote a shopping list: milk, eggs, bread, and butter. When she got to the store, she realized she had "
                "forgotten the list at home. She called her husband and asked him to read it to her. He said, 'I can't find it. "
                "Where did you leave it?' She replied, 'On the kitchen counter, next to the milk, eggs, bread, and butter.'"
            ),
            "vi": (
                "Một phụ nữ viết danh sách mua sắm: sữa, trứng, bánh mì, và bơ. Khi cô đến cửa hàng, cô nhận ra cô đã "
                "quên danh sách ở nhà. Cô gọi chồng và yêu cầu anh đọc cho cô. Anh nói, 'Anh không tìm thấy. "
                "Em để nó ở đâu?' Cô trả lời, 'Trên quầy bếp, bên cạnh sữa, trứng, bánh mì, và bơ.'"
            ),
        },
    },
    {
        "name": "The GPS Navigation",
        "bookNote": {
            "en": (
                "A man was following GPS directions to a restaurant. The GPS told him to turn left, but he turned right by "
                "mistake. The GPS said, 'Recalculating route.' He turned around and went back. The GPS said, 'Recalculating "
                "route.' He thought, 'This GPS is as confused as I am!'"
            ),
            "vi": (
                "Một người đàn ông đang theo chỉ dẫn GPS đến một nhà hàng. GPS bảo anh rẽ trái, nhưng anh rẽ phải do "
                "nhầm lẫn. GPS nói, 'Tính toán lại tuyến đường.' Anh quay lại và đi ngược. GPS nói, 'Tính toán lại "
                "tuyến đường.' Anh nghĩ, 'GPS này bối rối như tôi vậy!'"
            ),
        },
    },
    {
        "name": "The Restaurant Bill",
        "bookNote": {
            "en": (
                "A couple went to a restaurant and ordered dinner. When the bill came, the man was shocked to see it was $200. "
                "He asked the waiter, 'Is this correct?' The waiter replied, 'Yes, sir. You ordered the most expensive items "
                "on the menu.' The man said, 'I thought the prices were in cents, not dollars!'"
            ),
            "vi": (
                "Một cặp đôi đến nhà hàng và gọi bữa tối. Khi hóa đơn đến, người đàn ông sốc khi thấy nó là 200 đô. "
                "Anh hỏi người phục vụ, 'Có đúng không?' Người phục vụ trả lời, 'Vâng, thưa ông. Ông đã gọi những món đắt nhất "
                "trong thực đơn.' Người đàn ông nói, 'Tôi nghĩ giá tính bằng xu, không phải đô la!'"
            ),
        },
    },
    {
        "name": "The Movie Ticket",
        "bookNote": {
            "en": (
                "A man bought a movie ticket and went to see the film. Halfway through, he realized he was in the wrong "
                "theater. He was watching a romantic comedy, but he had bought a ticket for an action movie. He thought, 'Well, "
                "at least this movie is better than the one I paid for!'"
            ),
            "vi": (
                "Một người đàn ông mua vé xem phim và đi xem phim. Nửa chừng, anh nhận ra anh đang ở rạp "
                "sai. Anh đang xem một bộ phim hài lãng mạn, nhưng anh đã mua vé cho một bộ phim hành động. Anh nghĩ, 'Ồ, "
                "ít nhất bộ phim này hay hơn bộ phim tôi đã trả tiền!'"
            ),
        },
    },
    {
        "name": "The Dry Cleaner",
        "bookNote": {
            "en": (
                "A man took his suit to the dry cleaner and asked them to remove a stain. When he picked it up, the stain was "
                "gone, but there was a hole where the stain had been. He asked, 'What happened?' The dry cleaner said, 'We had "
                "to cut it out. The stain was too stubborn.'"
            ),
            "vi": (
                "Một người đàn ông mang bộ vest đến tiệm giặt khô và yêu cầu họ loại bỏ vết bẩn. Khi anh nhận nó, vết bẩn đã "
                "biến mất, nhưng có một lỗ nơi vết bẩn đã từng ở. Anh hỏi, 'Chuyện gì đã xảy ra?' Người giặt khô nói, 'Chúng tôi phải "
                "cắt nó ra. Vết bẩn quá cứng đầu.'"
            ),
        },
    },
    {
        "name": "The Haircut",
        "bookNote": {
            "en": (
                "A man went to a barber and asked for a trim. The barber cut his hair too short. The man said, 'I asked for a "
                "trim, not a buzz cut!' The barber replied, 'I'm sorry, but your hair was so long, I got carried away. But look "
                "on the bright side—you'll save money on shampoo!'"
            ),
            "vi": (
                "Một người đàn ông đến thợ cắt tóc và yêu cầu cắt tỉa. Người thợ cắt tóc cắt tóc anh quá ngắn. Người đàn ông nói, 'Tôi yêu cầu một "
                "lần cắt tỉa, không phải cắt trọc!' Người thợ cắt tóc trả lời, 'Tôi xin lỗi, nhưng tóc của bạn quá dài, tôi đã quá tay. Nhưng nhìn "
                "mặt tích cực—bạn sẽ tiết kiệm tiền cho dầu gội đầu!'"
            ),
        },
    },
    {
        "name": "The Taxi Driver",
        "bookNote": {
            "en": (
                "A man got into a taxi and told the driver his destination. The driver started driving in the opposite "
                "direction. The man said, 'You're going the wrong way!' The driver replied, 'I know, but I'm new to this city. "
                "I'm just exploring!'"
            ),
            "vi": (
                "Một người đàn ông lên taxi và nói với tài xế điểm đến của mình. Tài xế bắt đầu lái theo hướng ngược lại. "
                "Người đàn ông nói, 'Anh đang đi sai đường!' Tài xế trả lời, 'Tôi biết, nhưng tôi mới đến thành phố này. "
                "Tôi chỉ đang khám phá!'"
            ),
        },
    },
    {
        "name": "The Elevator",
        "bookNote": {
            "en": (
                "A man got into an elevator and pressed the button for the 10th floor. The elevator went up to the 15th floor "
                "instead. He pressed the button again, and it went down to the 5th floor. He thought, 'This elevator has a mind "
                "of its own!'"
            ),
            "vi": (
                "Một người đàn ông bước vào thang máy và nhấn nút tầng 10. Thang máy đi lên tầng 15 "
                "thay vì. Anh nhấn nút lại, và nó đi xuống tầng 5. Anh nghĩ, 'Thang máy này có tâm trí riêng "
                "của nó!'"
            ),
        },
    },
    {
        "name": "The Hotel Room",
        "bookNote": {
            "en": (
                "A man checked into a hotel and was given room 101. When he opened the door, he saw another person already in "
                "the room. He said, 'I'm sorry, I think there's been a mistake.' The other person said, 'No mistake. This is my "
                "room. You must have the wrong number.' The man checked his key card—it said room 110."
            ),
            "vi": (
                "Một người đàn ông check-in khách sạn và được cho phòng 101. Khi anh mở cửa, anh thấy một người khác đã ở trong "
                "phòng. Anh nói, 'Tôi xin lỗi, tôi nghĩ có nhầm lẫn.' Người kia nói, 'Không nhầm. Đây là "
                "phòng của tôi. Bạn chắc có số sai.' Người đàn ông kiểm tra thẻ khóa—nó nói phòng 110."
            ),
        },
    },
    {
        "name": "The Package Delivery",
        "bookNote": {
            "en": (
                "A man was expecting a package delivery. The delivery person left a note saying, 'Package delivered to your "
                "neighbor.' The man went to his neighbor's house to get the package. His neighbor said, 'I don't have your "
                "package. I think the delivery person got the wrong address.'"
            ),
            "vi": (
                "Một người đàn ông đang chờ giao hàng. Người giao hàng để lại một mảnh giấy nói, 'Gói hàng đã giao cho "
                "hàng xóm của bạn.' Người đàn ông đến nhà hàng xóm để lấy gói hàng. Hàng xóm của anh nói, 'Tôi không có "
                "gói hàng của bạn. Tôi nghĩ người giao hàng đã nhầm địa chỉ.'"
            ),
        },
    },
    {
        "name": "The ATM Machine",
        "bookNote": {
            "en": (
                "A man went to an ATM to withdraw money. He inserted his card and entered his PIN. The machine said, 'Insufficient "
                "funds.' He thought, 'That's strange. I just deposited money yesterday.' Then he realized he was using his "
                "credit card instead of his debit card."
            ),
            "vi": (
                "Một người đàn ông đến máy ATM để rút tiền. Anh cắm thẻ và nhập mã PIN. Máy nói, 'Không đủ "
                "tiền.' Anh nghĩ, 'Lạ nhỉ. Tôi vừa gửi tiền hôm qua.' Sau đó anh nhận ra anh đang dùng "
                "thẻ tín dụng thay vì thẻ ghi nợ."
            ),
        },
    },
    {
        "name": "The Coffee Shop",
        "bookNote": {
            "en": (
                "A man ordered a large coffee at a coffee shop. The barista gave him a small coffee instead. He said, 'I ordered "
                "a large coffee.' The barista replied, 'I'm sorry, but we're out of large cups. This is the largest we have.' "
                "The man thought, 'Then why do you have a large option on the menu?'"
            ),
            "vi": (
                "Một người đàn ông gọi một ly cà phê lớn tại quán cà phê. Người phục vụ đưa cho anh một ly cà phê nhỏ thay vì. Anh nói, 'Tôi gọi "
                "một ly cà phê lớn.' Người phục vụ trả lời, 'Tôi xin lỗi, nhưng chúng tôi hết ly lớn. Đây là ly lớn nhất chúng tôi có.' "
                "Người đàn ông nghĩ, 'Vậy tại sao bạn có tùy chọn lớn trong thực đơn?'"
            ),
        },
    },
    {
        "name": "The Parking Space",
        "bookNote": {
            "en": (
                "A man found a parking space and started to park his car. Another car pulled in from the other side and took the "
                "space. The man said, 'I was here first!' The other driver said, 'I don't see your name on it!' The man "
                "replied, 'I don't see yours either!'"
            ),
            "vi": (
                "Một người đàn ông tìm thấy chỗ đỗ xe và bắt đầu đỗ xe. Một chiếc xe khác kéo vào từ phía bên kia và chiếm "
                "chỗ. Người đàn ông nói, 'Tôi đến trước!' Người lái xe kia nói, 'Tôi không thấy tên bạn trên đó!' Người đàn ông "
                "trả lời, 'Tôi cũng không thấy tên bạn!'"
            ),
        },
    },
    {
        "name": "The Grocery Store",
        "bookNote": {
            "en": (
                "A man went to the grocery store to buy milk. He walked up and down the aisles but couldn't find it. He asked a "
                "store employee, 'Where is the milk?' The employee said, 'It's in the dairy section, aisle 3.' The man said, "
                "'I'm in aisle 3, and I don't see it.' The employee said, 'That's because you're in the frozen food section.'"
            ),
            "vi": (
                "Một người đàn ông đến cửa hàng tạp hóa để mua sữa. Anh đi lên xuống các lối đi nhưng không tìm thấy. Anh hỏi một "
                "nhân viên cửa hàng, 'Sữa ở đâu?' Nhân viên nói, 'Nó ở khu sữa, lối đi 3.' Người đàn ông nói, "
                "'Tôi đang ở lối đi 3, và tôi không thấy nó.' Nhân viên nói, 'Đó là vì bạn đang ở khu thực phẩm đông lạnh.'"
            ),
        },
    },
    {
        "name": "The Doctor's Appointment",
        "bookNote": {
            "en": (
                "A man made a doctor's appointment for 2 PM. He arrived at 2:30 PM and was told he was late. He said, 'I'm only "
                "30 minutes late.' The receptionist said, 'Yes, but your appointment was for 2 PM, not 2:30 PM.' The man "
                "replied, 'I know, but I thought doctors were always running late, so I thought I'd be on time if I came late!'"
            ),
            "vi": (
                "Một người đàn ông đặt lịch hẹn bác sĩ lúc 2 giờ chiều. Anh đến lúc 2:30 chiều và được báo là muộn. Anh nói, 'Tôi chỉ "
                "muộn 30 phút.' Người tiếp tân nói, 'Vâng, nhưng cuộc hẹn của bạn là lúc 2 giờ chiều, không phải 2:30 chiều.' Người đàn ông "
                "trả lời, 'Tôi biết, nhưng tôi nghĩ bác sĩ luôn muộn, vì vậy tôi nghĩ tôi sẽ đúng giờ nếu tôi đến muộn!'"
            ),
        },
    },
    {
        "name": "The Restaurant Reservation",
        "bookNote": {
            "en": (
                "A couple made a restaurant reservation for 7 PM. When they arrived, the restaurant was closed. They called the "
                "restaurant and asked why it was closed. The manager said, 'We're closed on Mondays.' The couple said, 'But "
                "today is Tuesday!' The manager replied, 'I know, but we're still closed.'"
            ),
            "vi": (
                "Một cặp đôi đặt bàn nhà hàng lúc 7 giờ tối. Khi họ đến, nhà hàng đã đóng cửa. Họ gọi "
                "nhà hàng và hỏi tại sao nó đóng cửa. Người quản lý nói, 'Chúng tôi đóng cửa vào thứ Hai.' Cặp đôi nói, 'Nhưng "
                "hôm nay là thứ Ba!' Người quản lý trả lời, 'Tôi biết, nhưng chúng tôi vẫn đóng cửa.'"
            ),
        },
    },
    {
        "name": "The Movie Theater",
        "bookNote": {
            "en": (
                "A man went to a movie theater and bought a ticket. When he entered the theater, he saw that the movie had "
                "already started. He asked an usher, 'When did the movie start?' The usher said, 'About 20 minutes ago.' The "
                "man said, 'But the ticket says 7 PM!' The usher replied, 'Yes, but the movie started at 6:40 PM.'"
            ),
            "vi": (
                "Một người đàn ông đến rạp chiếu phim và mua vé. Khi anh bước vào rạp, anh thấy bộ phim đã "
                "bắt đầu rồi. Anh hỏi người soát vé, 'Bộ phim bắt đầu lúc nào?' Người soát vé nói, 'Khoảng 20 phút trước.' "
                "Người đàn ông nói, 'Nhưng vé nói 7 giờ tối!' Người soát vé trả lời, 'Vâng, nhưng bộ phim bắt đầu lúc 6:40 tối.'"
            ),
        },
    },
    {
        "name": "The Gas Station",
        "bookNote": {
            "en": (
                "A man pulled into a gas station and asked the attendant to fill up his car. The attendant said, 'I'm sorry, but "
                "we're out of gas.' The man said, 'But you're a gas station!' The attendant replied, 'I know, but we ran out "
                "this morning. The delivery truck is late.'"
            ),
            "vi": (
                "Một người ghé trạm xăng và nhờ nhân viên đổ đầy bình. Nhân viên nói: 'Xin lỗi, chúng tôi hết xăng rồi.' "
                "Ông ấy thắc mắc: 'Nhưng đây là trạm xăng mà!' Nhân viên đáp: 'Tôi biết, nhưng chúng tôi đã hết hàng từ "
                "sáng nay. Xe tải giao xăng đang tới trễ.'"
            ),
        },
    },
]
# =======================================

output_dir = Path("stories")
output_dir.mkdir(parents=True, exist_ok=True)

def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "story"


def normalize_book_note(story: dict) -> dict:
    note = story.get("bookNote")
    if isinstance(note, dict):
        return {
            "en": note.get("en", ""),
            "vi": note.get("vi", ""),
        }
    return {
        "en": story.get("bookNote_en", note or ""),
        "vi": story.get("bookNote_vi", ""),
    }

for index, story in enumerate(stories, start=1):
    base_slug = slugify(story["name"])
    filename = output_dir / f"{index:02d}-{base_slug}.txt"
    payload = {
        "name": story["name"],
        "bookNote": normalize_book_note(story),
        "bookSections": [],
        "chapters": [],
    }
    with filename.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Saved JSON to {filename.resolve()}")
