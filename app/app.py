from fastapi import FastAPI, HTTPException
app = FastAPI()

text_posts = {
    1:{
        "title" : "THIS IS A CRIME 🇮🇹🔥",
        "content" : "Pineapple on pizza is an attack on Italy. My ancestors didn’t build culinary perfection for you to throw fruit on it. Stop the madness."
    },
    2:{
        "title" : "Sweet + Salty = PERFECTION 🍍❤️",
        "content" : "Tomato is acidic. Cheese is fatty. Pineapple is sweet. That balance is science. You’re not protecting tradition — you’re afraid of flavor."
    },
    3:{
        "title" : "Nonna Just Closed The Restaurant 😭",
        "content" : "If my grandmother saw pineapple on pizza she would disown the entire bloodline. Some things are sacred."
    },
    4:{
        "title" : "Food Is Not A Museum 🧨",
        "content" : "Stop acting like pizza is a historical artifact. It’s dough and toppings. Let it evolve."
    },
    5:{
        "title" : "It’s Disgusting. Period.",
        "content" : "Hot fruit. Melted cheese. Soggy crust. No. Absolutely not. There are limits."
    },
    6:{
        "title" : "The Haters Eat It In Secret 👀",
        "content" : "Funny how pineapple pizza always disappears first at parties. Loud critics. Quiet chewers."
    },
    7:{
        "title" : "You’re Just Being Elitist 🍕",
        "content" : "People pretending they’re Michelin chefs over a takeaway pizza. Relax. It’s not that deep."
    },
    8:{
        "title" : "Fusion Is The Future 🌏",
        "content" : "Asia mixes sweet and savory every day. The world moves forward. Pizza can too."
    },
    9:{
        "title" : "Call It Something Else",
        "content" : "Flatbread with fruit? Fine. But don’t call it pizza. Words matter."
    },
    10:{
        "title" : "I Will Die On This Hill 🍍🔥",
        "content" : "Pineapple on pizza is elite. I don’t care who judges me. I will order it every time."
    }
}

@app.get("/posts")
def read_all_posts():
    return text_posts

@app.get("/posts/{id}")
def read_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not Found")
    return text_posts.get(id)