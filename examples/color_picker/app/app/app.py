import pynecone as pc
import pynecone_helper

class State(pc.State):
    color = "#aabbcc"

def index():
    #print(pynecone_helper.color_picker(on_change=State.set_color)) #
    #print(type(pynecone_helper.color_picker(on_change=State.set_color))) #    
    return pc.box(
        pc.vstack(
            pc.text(State.color),
            pynecone_helper.color_picker(on_change=State.set_color),
        ),
        background_color=State.color,
        padding="5em",
        border_radius="1em",
    )

app = pc.App(state=State)
app.add_page(index, title="Color picker")
app.compile()
