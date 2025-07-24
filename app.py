import streamlit as st
from datetime import datetime
from database import criar_banco
from sistema import SistemaReservas
from models import Sala, Usuario, Reserva

criar_banco()
sistema = SistemaReservas()

st.title("📅 Sistema de Reserva de Salas de Reunião")

menu = st.sidebar.selectbox("Menu", ["Cadastrar Sala", "Cadastrar Usuário", "Nova Reserva", "Ver Reservas", "Cancelar Reserva"])

if menu == "Cadastrar Sala":
    st.header("Cadastrar nova sala")
    nome_sala = st.text_input("Nome da sala")
    if st.button("Adicionar sala"):
        if nome_sala.strip():
            sistema.adicionar_sala(Sala(nome_sala.strip()))
            st.success(f"Sala '{nome_sala}' adicionada com sucesso!")
        else:
            st.error("Nome da sala não pode ser vazio")

elif menu == "Cadastrar Usuário":
    st.header("Cadastrar novo usuário")
    nome_usuario = st.text_input("Nome do usuário")
    email_usuario = st.text_input("Email do usuário")
    if st.button("Adicionar usuário"):
        if nome_usuario.strip() and email_usuario.strip():
            sistema.adicionar_usuario(Usuario(nome_usuario.strip(), email_usuario.strip()))
            st.success(f"Usuário '{nome_usuario}' adicionado com sucesso!")
        else:
            st.error("Nome e email são obrigatórios")

elif menu == "Nova Reserva":
    st.header("Fazer uma nova reserva")
    salas = sistema.listar_salas()
    usuarios = sistema.listar_usuarios()

    if not salas:
        st.warning("Nenhuma sala cadastrada. Cadastre uma sala primeiro.")
        st.stop()
    if not usuarios:
        st.warning("Nenhum usuário cadastrado. Cadastre um usuário primeiro.")
        st.stop()

    sala_selecionada = st.selectbox("Selecione a sala", [s.nome for s in salas])
    usuario_selecionado = st.selectbox("Selecione o usuário", [u.nome for u in usuarios])
    data_reserva = st.date_input("Data da reserva")
    inicio_reserva = st.time_input("Hora de início")
    fim_reserva = st.time_input("Hora de fim")

    if fim_reserva <= inicio_reserva:
        st.error("A hora de fim deve ser maior que a hora de início")
    else:
        if st.button("Reservar"):
            sala_obj = next(s for s in salas if s.nome == sala_selecionada)
            usuario_obj = next(u for u in usuarios if u.nome == usuario_selecionado)
            inicio_str = inicio_reserva.strftime("%H:%M")
            fim_str = fim_reserva.strftime("%H:%M")
            data_str = data_reserva.strftime("%Y-%m-%d")
            reserva = Reserva(sala_obj.id, usuario_obj.id, data_str, inicio_str, fim_str)
            if sistema.adicionar_reserva(reserva):
                st.success("Reserva feita com sucesso!")
            else:
                st.error("Conflito de horário para essa sala.")

elif menu == "Ver Reservas":
    st.header("Reservas cadastradas")
    data_filtro = st.date_input("Filtrar por data (opcional)")
    reservas = sistema.listar_reservas(data=data_filtro.strftime("%Y-%m-%d"))
    if reservas:
        for r in reservas:
            st.write(f"ID: {r[0]} | Sala: {r[1]} | Usuário: {r[2]} | Data: {r[3]} | Início: {r[4]} | Fim: {r[5]}")
    else:
        st.info("Nenhuma reserva encontrada para a data selecionada.")

elif menu == "Cancelar Reserva":
    st.header("Cancelar reserva existente")
    reservas = sistema.listar_reservas()
    reserva_ids = [r[0] for r in reservas]
    reserva_desc = [f"ID: {r[0]} | Sala: {r[1]} | Usuário: {r[2]} | Data: {r[3]} | {r[4]}-{r[5]}" for r in reservas]
    reserva_selecionada = st.selectbox("Selecione a reserva para cancelar", reserva_desc)
    idx = reserva_desc.index(reserva_selecionada)
    reserva_id = reserva_ids[idx]
    if st.button("Cancelar reserva"):
        sistema.cancelar_reserva(reserva_id)
        st.success("Reserva cancelada com sucesso!")
