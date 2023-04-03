from st_aggrid import AgGrid
from streamlit_option_menu import option_menu
import streamlit as st
import sqlite3 as lite
import pandas as pd





conn = lite.connect('banco.db')
cur = conn.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS Cadastro(NOME text, APELIDO TEXT, RESIDENCIA TEXT, IDADE INT, CONTACTO TEXT, ESTATUS TEXT, ESTADO CÍVIL TEXT, POSIÇAO TEXT)''')
st.set_page_config(page_title="IGREJA WESLEYANA-NAMPULA")
#with st.sidebar:
Selecao = st.sidebar.selectbox(
    "MENU",
    ["INÍCIO","CADASTRO","MEMBROS","CONTACTO"],
   
)


if Selecao=="INÍCIO":
    st.header(body=":green[IGREJA EMMANUEL EVANGÉLICA WESLEYANA DE NAMPULA]")
    st.header(body=":orange[SEJA BEM-VINDO - WELL-COME]")
                
                
    st.subheader(body=":red[SALMOS 87:6]")
    st.title(body=":green[Assim o :red[SENHOR] escreverá no registro dos povos: ' Este nasceu ali ']")
    fotos = "Igreja.jfif"
    st.image(fotos)
                
if   Selecao == "CADASTRO":
    def Formulario():
        global Nome, Apelido, Residencia, Idade, Contacto, Estado, Estado2, Posicao
        
        with st.form(key="Formulario de Cadastro", clear_on_submit=True):
            col1, col2, =st.columns(2)
            with col1:
                    #Id = st.number_input("Crie o seu Id")
                Nome =st.text_input(':green[Informe o seu Nome:]')
                Apelido =st.text_input(":green[Informe o seu Apelido:] ")
                Residencia = st.text_input(':green[Informe a sua Residencia:] ')
                Idade = st.text_input(':green[Informe a sua Idade:] ')
                        
            with col2:
                    Contacto = st.text_input(":green[Informe o seu contacto:] ")
                    Estado = st.selectbox(":green[Selecione uma opçao]",("Selecione","Batizada","Batizado","Nao Batizada","Nao Batizado"))
                    Estado2 = st.selectbox(":green[Informe o seu Estado Cívil]",("Selecione","Solteira","Solteiro","Casada","Casado",))
                    Posicao = st.text_input(":green[Informe a sua Posiçao]")
                    Botao =st.form_submit_button(label="Submeter")
                        
            if  Botao ==True:
                Inserir(Nome, Apelido, Residencia, Idade, Contacto, Estado, Estado2, Posicao)
                st.success(body="Os seus dados foram inseridos com Sucesso",icon="✅")

            
   
    
            
        def Inserir(a,b,c,d,e,f,g,h):
        
            conn = lite.connect('banco.db')
            cur = conn.cursor()
            cur.execute(" INSERT INTO Cadastro VALUES('"+Nome+"','"+Apelido+"','"+Residencia+"','"+Idade+"','"+Contacto+"','"+Estado+"','"+Estado2+"','"+Posicao+"')")
            conn.commit()
            Dados=cur.execute("SELECT * FROM Cadastro")
            #Resultado = Dados.fetchall()
            #conn.close()
            
    Formulario(Nome, Apelido, Residencia, Idade, Contacto, Estado, Estado2, Posicao)
if Selecao == "MEMBROS":
        try:
            dt = pd.read_sql_query("SELECT * FROM Cadastro",conn)
            df2 = pd.DataFrame(dt, columns=['NOME', 'APELIDO', 'RESIDENCIA', 'IDADE', 'CONTACTO', 'ESTATUS', 'ESTADO', 'POSIÇAO'])
            st.dataframe(df2)
            st.info(f"Já foram Cadastrados até já, {len(df2)} Membros")
        except:
            pass

if Selecao=="CONTACTO":
        st.header(body="Envie-nos uma Mensagem")
        #foto = "Imagem.PNG"
        #st.image(foto)
        Emial = ''' 
        <form action="https://formsubmit.co/apoiocodeminde@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="nome" placeholder="Informe o seu Nome" required>
            <input type="email" placeholder="Seu Email!" required>
            <textarea name="message" placeholder="Envie sua Mensagem Aqui!" rows="10" required></textarea>
            <button type="submit">ENVIAR</button>
            
        
        
        
        </form>
        '''
    
        st.markdown(Emial, unsafe_allow_html=True)
        def Local_Css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        Local_Css("style.css.txt")

    
