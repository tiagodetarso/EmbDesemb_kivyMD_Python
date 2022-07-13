# para rodar é necessário ter instalado a versão 8.2.0 do pillow
# Para instalar = pip install pillow==8.2.0
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class Embaralhar_Mensagem(MDApp):
    def inverter_funcao(self):
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Desembaralhar Mensagens"
            self.input.text = "Digite aqui"
            #self.textoalterado.text = ""
            self.textoindicativo.text = ""
        
        else:
            self.state = 0
            self.toolbar.title = "Embaralhar Mensagens"
            self.input.text = "Digite aqui"
            #self.textoalterado.text = ""
            self.textoindicativo.text = ""
       
    def criptografar(self, args):
        if self.state == 0:
            linhas = 4
            mensagem = self.input.text
            while len(mensagem) % linhas != 0 and linhas<=10:
                if linhas >=10:
                    mensagem = mensagem+"!"
                    linhas = 3
                linhas+=1
            colunas= len(mensagem)/linhas
            colunas= int(colunas)
            i=0
            lista = []
            while i<colunas:
                lista.append(mensagem[i::colunas])
                i+=1
            criptografado=(''.join(lista))
            self.textoalterado.text = criptografado
            self.textoindicativo.text = "O resultado é:"
        else:
            linhas= 4
            mensagem = self.input.text
            while len(mensagem) % linhas != 0 and linhas<=10:
                if linhas >=10:
                    mensagem = mensagem+"!"
                    linhas = 3
                linhas+=1
            colunas= len(mensagem)/linhas
            colunas= int(colunas)
            i=0
            lista = []
            while i<linhas:
                lista.append(mensagem[i::linhas])
                i+=1
            descriptografado = (''.join(lista))
            self.textoalterado.text = descriptografado
            self.textoindicativo.text = "O resultado é:"

    def build (self):
        self.state = 0
        self.theme_cls.primary_palette = "Teal"
        screen = MDScreen()
        
        #top toolbar
        self.toolbar = MDToolbar(title = "Embaralhar Mensagens")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x: self.inverter_funcao()]]
        screen.add_widget(self.toolbar)
        
        self.nomeapp = MDLabel(
            text = "Emdesemb",
            halign = "center",
            pos_hint = {"center_x": 0.5, "center_y": 0.9},
            font_size = 50
            )
        
        #Logo
        """
        screen.add_widget(Image(
            source = "Encrip.png",
            pos_hint = {"center_x": 0.5, "center_y": 0.75},
            size_hint = (1, 1)
            ))"""
        
        self.input = MDTextField(
            text = "Digite aqui",
            halign = "center",
            size_hint = (0.9, 1),
            pos_hint = {"center_x": 0.5, "center_y": 0.6},
            font_size = 30
            )
        
        screen.add_widget(self.input)
        
        self.textoindicativo = MDLabel(
            text = "",
            halign = "center",
            pos_hint = {"center_x": 0.5, "center_y": 0.55},
            theme_text_color = "Secondary"
            )
        
        self.textoalterado = MDLabel(
            text = "",
            halign = "center",
            pos_hint = {"center_x": 0.5, "center_y": 0.50},
            theme_text_color = "Primary",
            font_style = "H6"
            )
        
        screen.add_widget(self.textoindicativo)
        screen.add_widget(self.textoalterado)
        
        screen.add_widget(MDFillRoundFlatButton(
            text = "Embaralhar / Desembaralhar",
            font_size = 25,
            pos_hint = {"center_x": 0.5, "center_y": 0.10},
            size_hint = (0.7,0.1),
            on_press = self.criptografar
            ))
        return screen

if __name__ == "__main__":
    Embaralhar_Mensagem().run()