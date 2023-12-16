--
-- PostgreSQL database dump
--

-- Dumped from database version 15.5 (Debian 15.5-1.pgdg120+1)
-- Dumped by pg_dump version 15.5 (Debian 15.5-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: dealtype; Type: TYPE; Schema: public; Owner: postgress
--

CREATE TYPE public.dealtype AS ENUM (
    'buy',
    'sell'
);


ALTER TYPE public.dealtype OWNER TO postgress;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgress
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgress;

--
-- Name: bots; Type: TABLE; Schema: public; Owner: postgress
--

CREATE TABLE public.bots (
    user_id uuid NOT NULL,
    instrument_code character varying(30) NOT NULL,
    status boolean DEFAULT false NOT NULL,
    start_balance numeric
);


ALTER TABLE public.bots OWNER TO postgress;

--
-- Name: deals; Type: TABLE; Schema: public; Owner: postgress
--

CREATE TABLE public.deals (
    id integer NOT NULL,
    price numeric NOT NULL,
    quantity integer NOT NULL,
    deal_type public.dealtype NOT NULL,
    user_id uuid NOT NULL,
    instrument_code character varying(30) NOT NULL,
    date_time timestamp without time zone DEFAULT now() NOT NULL,
    balance numeric
);


ALTER TABLE public.deals OWNER TO postgress;

--
-- Name: deals_id_seq; Type: SEQUENCE; Schema: public; Owner: postgress
--

CREATE SEQUENCE public.deals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.deals_id_seq OWNER TO postgress;

--
-- Name: deals_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgress
--

ALTER SEQUENCE public.deals_id_seq OWNED BY public.deals.id;


--
-- Name: instruments; Type: TABLE; Schema: public; Owner: postgress
--

CREATE TABLE public.instruments (
    code character varying(30) NOT NULL,
    title character varying NOT NULL,
    "group" character varying(30) NOT NULL,
    has_model boolean DEFAULT false NOT NULL
);


ALTER TABLE public.instruments OWNER TO postgress;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgress
--

CREATE TABLE public.users (
    id uuid NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    email character varying(100) NOT NULL,
    password character varying NOT NULL
);


ALTER TABLE public.users OWNER TO postgress;

--
-- Name: deals id; Type: DEFAULT; Schema: public; Owner: postgress
--

ALTER TABLE ONLY public.deals ALTER COLUMN id SET DEFAULT nextval('public.deals_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgress
--

COPY public.alembic_version (version_num) FROM stdin;
81ef4e3e725b
\.


--
-- Data for Name: bots; Type: TABLE DATA; Schema: public; Owner: postgress
--

COPY public.bots (user_id, instrument_code, status, start_balance) FROM stdin;
332097ee-807e-4958-b053-1bbf8c35e846	AMEZ	t	\N
332097ee-807e-4958-b053-1bbf8c35e846	MAGEP	f	\N
332097ee-807e-4958-b053-1bbf8c35e846	SBER	f	\N
\.


--
-- Data for Name: deals; Type: TABLE DATA; Schema: public; Owner: postgress
--

COPY public.deals (id, price, quantity, deal_type, user_id, instrument_code, date_time, balance) FROM stdin;
64	268.61	37	buy	332097ee-807e-4958-b053-1bbf8c35e846	SBER	2023-12-09 18:09:34.647626	61.43000000000029
65	266.02	37	sell	332097ee-807e-4958-b053-1bbf8c35e846	SBER	2023-12-09 18:09:34.697143	9904.17
66	265.04	37	buy	332097ee-807e-4958-b053-1bbf8c35e846	SBER	2023-12-09 18:09:34.736006	97.68999999999869
67	265.26	37	sell	332097ee-807e-4958-b053-1bbf8c35e846	SBER	2023-12-09 18:09:34.776246	9912.309999999998
68	267.75	37	buy	332097ee-807e-4958-b053-1bbf8c35e846	SBER	2023-12-09 18:09:34.827154	5.559999999997672
69	265.55	37	sell	332097ee-807e-4958-b053-1bbf8c35e846	SBER	2023-12-09 18:09:34.864233	9830.909999999998
70	264.95	37	buy	332097ee-807e-4958-b053-1bbf8c35e846	SBER	2023-12-09 18:09:34.903642	27.7599999999984
71	205.01	48	buy	332097ee-807e-4958-b053-1bbf8c35e846	WUSH	2023-12-09 18:10:50.049179	159.52000000000044
72	205.68	48	sell	332097ee-807e-4958-b053-1bbf8c35e846	WUSH	2023-12-09 18:10:50.076713	10032.16
73	206.47	48	buy	332097ee-807e-4958-b053-1bbf8c35e846	WUSH	2023-12-09 18:10:50.09281	121.60000000000036
74	207.69	48	sell	332097ee-807e-4958-b053-1bbf8c35e846	WUSH	2023-12-09 18:10:50.1089	10090.72
75	208.08	48	buy	332097ee-807e-4958-b053-1bbf8c35e846	WUSH	2023-12-09 18:10:50.120787	102.8799999999992
76	209.74	48	sell	332097ee-807e-4958-b053-1bbf8c35e846	WUSH	2023-12-09 18:10:50.177885	10170.4
77	209.91	48	buy	332097ee-807e-4958-b053-1bbf8c35e846	WUSH	2023-12-09 18:10:50.201647	94.71999999999935
78	209.0	48	sell	332097ee-807e-4958-b053-1bbf8c35e846	WUSH	2023-12-09 18:10:50.21808	10126.72
\.


--
-- Data for Name: instruments; Type: TABLE DATA; Schema: public; Owner: postgress
--

COPY public.instruments (code, title, "group", has_model) FROM stdin;
A-RM	Agilent TechnologiesORD SHS	stock_shares	t
BLK-RM	BlackRock Inc.	stock_shares	t
AIG-RM	American International ORD SHS	stock_shares	t
AMEZ	Ашинский метзавод ПАО ао	stock_shares	t
MAGEP	&quot;Магаданэнерго&quot; ПАО ап	stock_shares	t
SBER	Сбер Банк	stock_shares	t
WUSH	Whoosh 	stock_shares	t
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgress
--

COPY public.users (id, first_name, last_name, email, password) FROM stdin;
332097ee-807e-4958-b053-1bbf8c35e846	test	test	test1@example.com	$2b$12$mJ3lho3XeiKf2Le8EqNbvOfhDEkMgQ983zOMmKgJjXj/Os4qzcLjW
7f6d7fbe-e165-4681-86ca-7e75e2644b95	test2	test2	test2@example.com	$2b$12$8.iVwrn0IvEoi2INH0c6pOpp8aDqYuRDvP6GgGCkAyhhpX21fOGMe
17aa8cd1-2cdc-4060-911e-ee27be49e1be	rus	lan	123@test.com	$2b$12$6Gv5V9H6Ck5CE1iebONTduTu3lD0ifJJ6ySnXSnrczguP4O5KhspK
109b6a7b-b107-4752-a55d-1c552431097f	rus	lan	test@test.com	$2b$12$rsD2LJ6Z7Y15aViYhUVsQeHwnkqUrl3igyH0uy6VLQg/ljlg9OjXm
50040eba-7ee0-46a1-8939-07b14cf11256	Rus	Lan	123@ttt.com	$2b$12$l2RR/FdKWu9.5sHm93/jauaxBzz4TSjXTVTsU/.41J9/3Onbbo0WW
4deee21d-6f3c-4cea-bb54-f62277158a8e	sd	sadf	dd@dd.dd	$2b$12$LTstGEHwMQ7J3cph6pzdsuXOV37WfQV4lfJY/AfsmjKeZiBynCbBm
\.


--
-- Name: deals_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgress
--

SELECT pg_catalog.setval('public.deals_id_seq', 78, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgress
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: bots bots_pkey; Type: CONSTRAINT; Schema: public; Owner: postgress
--

ALTER TABLE ONLY public.bots
    ADD CONSTRAINT bots_pkey PRIMARY KEY (user_id, instrument_code);


--
-- Name: deals deals_pkey; Type: CONSTRAINT; Schema: public; Owner: postgress
--

ALTER TABLE ONLY public.deals
    ADD CONSTRAINT deals_pkey PRIMARY KEY (id);


--
-- Name: instruments instruments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgress
--

ALTER TABLE ONLY public.instruments
    ADD CONSTRAINT instruments_pkey PRIMARY KEY (code);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgress
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgress
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: bots bots_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgress
--

ALTER TABLE ONLY public.bots
    ADD CONSTRAINT bots_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: deals deals_instrument_code_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgress
--

ALTER TABLE ONLY public.deals
    ADD CONSTRAINT deals_instrument_code_fkey FOREIGN KEY (instrument_code) REFERENCES public.instruments(code);


--
-- Name: deals deals_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgress
--

ALTER TABLE ONLY public.deals
    ADD CONSTRAINT deals_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

