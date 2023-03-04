import pynecone as pc

'''
#https://github.com/omgovich/react-colorful#getting-started
#https://www.npmjs.com/package/react-colorful
import { HexColorPicker } from "react-colorful";

const YourComponent = () => {
  const [color, setColor] = useState("#aabbcc");
  return <HexColorPicker color={color} onChange={setColor} />;
};
'''
class ColorPicker(pc.Component): #pc.Component 상속
    library = "react-colorful" #npm 패키지 이름
    tag = "HexColorPicker" #리액트 컴포넌트의 태그 이름

    @classmethod  
    def get_controlled_triggers(cls):
        return {"on_change"}

color_picker = ColorPicker.create
