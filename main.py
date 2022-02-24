Topic = ["1. Nutrition","2. Calorie Counter"]
Calories_Males = {1:"1000",2:"1000",3:"1000 - 1400",4:"1200 - 1600",5:"1200 - 1600",6:"1400 - 1800",7:"1400 - 1800",8:"1400 - 2000",9:"1600 - 2000",10:"1600 - 2200",11:"1800 - 2200",12:"1800 - 2400",13:"2000 - 2600",14:"2000 - 2800",15:"2200 - 3000",16:"2400 - 3200",17:"2400 - 3200",18:"2400 - 3200"}
Calories_Females = {1:"1000",2:"1000",3:"",4:"1000 - 1400",5:"1200 - 1600",6:"1200 - 1600",7:"1200 - 1800",8:"1400 - 1800",9:"1400 - 1800",10:"1400 - 2000",11:"1600 - 2000",12:"1600 - 2200",13:"1600 - 2200",14:"1800 - 2400",15:"1800 - 2400",16:"1800 - 2400",17:"1800 - 2400",18:"1800 - 2400"}
Water = {range(1,2):8,range(3,8):40,range(9,13):60,range(14,18):80,range(19,100):92}
print("Choose a topic")
print(Topic)
Topic_input = input("")
Topic_input = Topic_input.lower()
Topic_input = Topic_input.strip()
if Topic_input == "calorie counter" or Topic_input == "2":
    print("Hello! To calculate how many calories you have burnt please answer the following questions")
    time = float(input("How many minutes did you do this exercise?"))
    MET = float(input("""How many MET's was this activity?
(metabolic equivalent of task)
To get an idea of how many MET's
Your activity was, try this link
https://www.hss.edu/images/corporate/burning-calories-1.jpg
"""))
    pound = float(input("How many pounds do you weigh?"))
    pound = pound * 0.453592
    Cal_Burnt = (time * MET * 3.5 * pound) / 200
    Cal_Burnt = int(Cal_Burnt)
    print("You would have burnt around",Cal_Burnt,"calories.")
    print("""Wash your hands frequently
Always wear a mask when outside
And maintain Social distancing of at least 6 feet""")
if Topic_input == "nutrition" or Topic_input == "1":
    Tools1 = ["a. Personalized Nutrition Guide","b. BMI Calculator"]
    print("Hello, please choose one of the tools")
    print(Tools1)
    N_input = input("")
    N_input = N_input.lower()
    if N_input == "bmi calculator" or N_input == "b":
        print("Hello and welcome to the BMI calculator please answer the following questions")
        weight = float(input("How many pounds do you weigh?"))
        height = float(input("How tall are you in inches?"))
        weight = weight * 0.45359237
        height = height * 0.0254
        BMI = weight/(height*height)
        print("You have a BMI of",BMI)
        BMI = int(BMI)
        if BMI > 25:
            print("You are overweight")
        if BMI < 18:
            print("You are underweight")
        if BMI in range(18,25):
            print("You have a healthy weight")
        print("""Wash your hands frequently
Always wear a mask when outside
And maintain Social distancing of at least 6 feet""")
    if N_input == "personalized nutrition guide" or N_input == "a":
        print("Hello! To calculate what you should be eating, first we need to ask a few quick questions.")
        age = int(input("What is your age?"))
        gender = input("What is your gender?")
        gender = gender.lower()
        print("Great! Here are your results.")
        CMK = Calories_Males.keys()
        CWK = Calories_Females.keys()
        CM2 = {range(19,20):"2600 - 3000",range(21,25):"2400 - 3000",range(26,30):"2400 - 3000",range(31,35):"2400 - 3000",range(36,40):"2400 - 2800",range(41,45):"2200 - 2800",range(46,50):"2200 - 2800",range(51,55):"2200 - 2800",range(56,60):"2200 - 2600",range(61,65):"2000 - 2600",range(66,75):"2000 - 2600",range(75,120):"2000 - 2400"}
        CW2 = {}
        CMK1 = CM2.keys()
        CWK1 = CW2.keys()
        if gender == "female":
            if age >= 19:
                for a in CWK1:
                    if age in a:
                        print("You need to be consuming around", CW2[a],"calories")
            else:
                for a in CWK:
                    if a == age:
                        print("You need to be consuming around",Calories_Females[a],"calories")
        if gender == "male":
            if age >= 19:
                for a in CMK1:
                    if age in a:
                        print("You need to be consuming around", CM2[a],"calories")
            else:
                for a in CMK:
                    if a == age:
                        print("You need to be consuming around",Calories_Males[a],"calories")
        WK = Water.keys()
        for a in WK:
            if age in a:
                print("You need around",Water[a],"ounces of water per day")
        if age == 1:
            print("""0-8 months:
Infants are recommended to consume
breast milk and/or infant formula from
birth to 6 months. After 6 months,
developmental cues will indicate when
the infant is ready to try solid food
such as iron-fortified cereal, fruit, or
vegetables. Infant stomachs are very small but growth
at this stage is rapid, so, infants should be fed several
times a day. Allow infants to self-regulate how much
they consume. Begin with a few Tablespoons of solid
food a day and increase as needed. Offer solid foods
slowly and individually

8-12 months:
Infants at this stage may be consuming foods from
all food groups. Servings may range from about 1/8
to 1/3 cup servings 2-3 times a day. At 10 months,
combination foods such as macaroni and cheese may
be introduced to the infant. Continue to expose the
infant to a variety of healthy foods and allow them to
self-regulate when and how much to consume.""")
        if age == 2:
            print("""Children ages 1 to 2 years old should be eating solid
foods. Breast-feeding can be continued at this age, but
solid food should be the main source to fulfill energy
needs. Children should be eating a well balanced diet,
similar to that of an adult, with a variety of fruits and
vegetables, whole grains, protein source foods, and
low-fat dairy. Children in this age range should be
consuming whole milk, unless overweight or obesity is
a concern. Children should eat three meals a day and may also 
eat one or two healthy snacks. Serving sizes should
be about one-quarter of an adult’s serving size.""")
        if age == 3:
            print("""3 year olds are recommended
to eat 1 cup of fruit and vegetables per day. The types and colors of vegetables
eaten should be varied throughout
the week and should include:
- dark green
- red and orange
- beans and peas
- starchy vegetables
Each type and color of vegetables
provides a unique set of nutrients
that are important for child growth.
2 cups of dairy is also recommended and
can take the form of milk and cheese. They
should also consume 3 ounces of grains such
as bread, wheat and rice, Half of the grains eaten should be
whole grains. And 2 ounces of protein
like beans and chicken""")
        if age in range(4,8):
            print("""Around 1 - 1.5 cups of fruits
and vegetables in recommended for ages 4 - 8.
The types and colors of vegetables
eaten should be varied throughout
the week and should include:
• dark green
• red and orange
• beans and peas
• starchy vegetables
Each type and color of vegetables
provides a unique set of nutrients
that are important for child growth.
2.5 cups in also needed and can take the form of 
milk, cheese, and other milk products.
5 ounces of grains is needed and can be bread, wheat,
and rice too! Half of the grains eaten should be
whole grains. And finally, you need 4 ounces of protein which can include beans,
eggs, nuts, and meat.""")
        if age in range(9,13):
            print("""You need 1.5 cups  of fruit, 
and 2.5 cups of vegetables. Canned,
fresh, or frozen foods are all good
options. The types and colors of vegetables
eaten should be varied throughout
the week and should include:
• dark green
• red and orange
• beans and peas
• starchy vegetables
Each type and color of vegetables
provides a unique set of nutrients
that are important for growth. 3 cups of
dairy can take the form of milk, cheese,
and yogurt. Along with 5 - 6 ounces of grains
which can be found in foods like crackers,
bread, and rice. Half of the grains eaten should be
whole grains. And finally, 5 ounces
of protein is needed which can mainly come from beans,
nuts, and meat""")
        if age in range(14,18):
            print("""1.5 - 2 cups of fruit is needed
along with 2.5 - 3 cups of vegetables.
The types and colors of vegetables
eaten should be varied throughout
the week and should include:
• dark green
• red and orange
• beans and peas
• starchy vegetables
Each type and color of vegetables
provides a unique set of nutrients
that are important for growth.
Along with that, 3 whole cups of dairy
is needed which can come in the form
of milk, cheese, and yogurt. Plus, there is grains which has
6 - 8 ounces in foods lke bread and crackers,
And finally, 5 ounces of protein is needed which 
can mainly come from beans,
nuts, and meat""")
        if age in range(19,30):
            print("""2 cups of fruit
is needed at this age along with 2.5 - 3 cups
of vegetables. The types and colors of vegetables
eaten should be varied throughout
the week and should include:
• dark green
• red and orange
• beans and peas
• starchy vegetables
Each type and color of vegetables
provides a unique set of nutrients
that are important for growth. Plus with 3
cups of dairy which can include milk, cheese,
and yogurt. And with 6 - 8 ounces of grains
which can be found in foods such as bread, crackers, and pasta.
Half of the grains eaten should be whole grains. 
And finally, there is 5.5 - 6.5 ounces of protein which
at this age should be coming from meats like chicken and fish,
along with nuts and beans.""")
        if age in range(31,50):
            print("""1.5 - 2 cups of fruit
in needed along with 2.5 - 3 cups of vegetables.
The types and colors of vegetables
eaten should be varied throughout
the week and should include:
• dark green
• red and orange
• beans and peas
• starchy vegetables
Each type and color of vegetables
provides a unique set of nutrients
that are important for growth.
3 cups of dairy should include
in foods like milk, cheese, and yogurt.
Grains are essential and are at 6 - 7 ounces
per day which can come in foods like
crackers, bread, and pasta. And finally, around
5 - 6 ounces of protein is needed which can 
come from mainly meat, beans, and nuts""")
            print("""Wash your hands frequently
Always wear a mask when outside
And maintain Social distancing of at least 6 feet""")
