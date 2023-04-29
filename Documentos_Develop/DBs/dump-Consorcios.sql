--
-- PostgreSQL database dump
--

-- Dumped from database version 12.14 (Ubuntu 12.14-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 14.2

-- Started on 2023-04-28 19:35:00

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

DROP DATABASE "Consorcios";
--
-- TOC entry 2991 (class 1262 OID 16385)
-- Name: Consorcios; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "Consorcios" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'C.UTF-8';


ALTER DATABASE "Consorcios" OWNER TO postgres;

\connect "Consorcios"

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
-- TOC entry 3 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 2992 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 207 (class 1259 OID 24697)
-- Name: amenities; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.amenities (
    id_ameni integer NOT NULL,
    descripcion character varying
);


ALTER TABLE public.amenities OWNER TO admin;

--
-- TOC entry 206 (class 1259 OID 24695)
-- Name: amenities_id_ameni_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.amenities_id_ameni_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.amenities_id_ameni_seq OWNER TO admin;

--
-- TOC entry 2993 (class 0 OID 0)
-- Dependencies: 206
-- Name: amenities_id_ameni_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.amenities_id_ameni_seq OWNED BY public.amenities.id_ameni;


--
-- TOC entry 208 (class 1259 OID 24707)
-- Name: edif_ameni; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.edif_ameni (
    edi_fk integer NOT NULL,
    ameni_fk integer NOT NULL
);


ALTER TABLE public.edif_ameni OWNER TO admin;

--
-- TOC entry 203 (class 1259 OID 24626)
-- Name: edificios; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.edificios (
    id_edif integer NOT NULL,
    pais character varying NOT NULL,
    pcia character varying NOT NULL,
    ciudad character varying NOT NULL,
    nombre character varying,
    direccion character varying NOT NULL
);


ALTER TABLE public.edificios OWNER TO admin;

--
-- TOC entry 202 (class 1259 OID 24624)
-- Name: edificios_id_edif_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.edificios_id_edif_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.edificios_id_edif_seq OWNER TO admin;

--
-- TOC entry 2994 (class 0 OID 0)
-- Dependencies: 202
-- Name: edificios_id_edif_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.edificios_id_edif_seq OWNED BY public.edificios.id_edif;


--
-- TOC entry 210 (class 1259 OID 24722)
-- Name: reclamos_sugerencias; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.reclamos_sugerencias (
    id_rec_sug integer NOT NULL,
    reclamo_sugerencia character varying NOT NULL,
    asunto character varying,
    descripcion character varying,
    edi_fk integer NOT NULL,
    uf_fk integer
);


ALTER TABLE public.reclamos_sugerencias OWNER TO admin;

--
-- TOC entry 209 (class 1259 OID 24720)
-- Name: reclamos_sugerencias_id_rec_sug_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.reclamos_sugerencias_id_rec_sug_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reclamos_sugerencias_id_rec_sug_seq OWNER TO admin;

--
-- TOC entry 2995 (class 0 OID 0)
-- Dependencies: 209
-- Name: reclamos_sugerencias_id_rec_sug_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.reclamos_sugerencias_id_rec_sug_seq OWNED BY public.reclamos_sugerencias.id_rec_sug;


--
-- TOC entry 212 (class 1259 OID 24748)
-- Name: reserva_ameni; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.reserva_ameni (
    id_reserva integer NOT NULL,
    fecha_dde date NOT NULL,
    hora_dde time without time zone NOT NULL,
    fecha_hasta date NOT NULL,
    hora_hasta time without time zone NOT NULL,
    edi_fk integer NOT NULL,
    uf_fk integer NOT NULL,
    ameni_fk integer NOT NULL
);


ALTER TABLE public.reserva_ameni OWNER TO admin;

--
-- TOC entry 211 (class 1259 OID 24746)
-- Name: reserva_ameni_id_reserva_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.reserva_ameni_id_reserva_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reserva_ameni_id_reserva_seq OWNER TO admin;

--
-- TOC entry 2996 (class 0 OID 0)
-- Dependencies: 211
-- Name: reserva_ameni_id_reserva_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.reserva_ameni_id_reserva_seq OWNED BY public.reserva_ameni.id_reserva;


--
-- TOC entry 205 (class 1259 OID 24641)
-- Name: unidad_funcional; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.unidad_funcional (
    id_uf integer NOT NULL,
    unidad_funcional character varying NOT NULL,
    uf_tipo character varying NOT NULL,
    piso character varying NOT NULL,
    dpto character varying NOT NULL,
    coprop_nombre character varying NOT NULL,
    porc_a character varying,
    porc_b character varying,
    porc_c character varying,
    porc_d character varying,
    edif_fk integer NOT NULL
);


ALTER TABLE public.unidad_funcional OWNER TO admin;

--
-- TOC entry 204 (class 1259 OID 24639)
-- Name: unidad_funcional_id_uf_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.unidad_funcional_id_uf_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.unidad_funcional_id_uf_seq OWNER TO admin;

--
-- TOC entry 2997 (class 0 OID 0)
-- Dependencies: 204
-- Name: unidad_funcional_id_uf_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.unidad_funcional_id_uf_seq OWNED BY public.unidad_funcional.id_uf;


--
-- TOC entry 2828 (class 2604 OID 24700)
-- Name: amenities id_ameni; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.amenities ALTER COLUMN id_ameni SET DEFAULT nextval('public.amenities_id_ameni_seq'::regclass);


--
-- TOC entry 2826 (class 2604 OID 24629)
-- Name: edificios id_edif; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.edificios ALTER COLUMN id_edif SET DEFAULT nextval('public.edificios_id_edif_seq'::regclass);


--
-- TOC entry 2829 (class 2604 OID 24725)
-- Name: reclamos_sugerencias id_rec_sug; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reclamos_sugerencias ALTER COLUMN id_rec_sug SET DEFAULT nextval('public.reclamos_sugerencias_id_rec_sug_seq'::regclass);


--
-- TOC entry 2830 (class 2604 OID 24751)
-- Name: reserva_ameni id_reserva; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reserva_ameni ALTER COLUMN id_reserva SET DEFAULT nextval('public.reserva_ameni_id_reserva_seq'::regclass);


--
-- TOC entry 2827 (class 2604 OID 24644)
-- Name: unidad_funcional id_uf; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.unidad_funcional ALTER COLUMN id_uf SET DEFAULT nextval('public.unidad_funcional_id_uf_seq'::regclass);


--
-- TOC entry 2980 (class 0 OID 24697)
-- Dependencies: 207
-- Data for Name: amenities; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.amenities (id_ameni, descripcion) FROM stdin;
\.


--
-- TOC entry 2981 (class 0 OID 24707)
-- Dependencies: 208
-- Data for Name: edif_ameni; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.edif_ameni (edi_fk, ameni_fk) FROM stdin;
\.


--
-- TOC entry 2976 (class 0 OID 24626)
-- Dependencies: 203
-- Data for Name: edificios; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.edificios (id_edif, pais, pcia, ciudad, nombre, direccion) FROM stdin;
\.


--
-- TOC entry 2983 (class 0 OID 24722)
-- Dependencies: 210
-- Data for Name: reclamos_sugerencias; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.reclamos_sugerencias (id_rec_sug, reclamo_sugerencia, asunto, descripcion, edi_fk, uf_fk) FROM stdin;
\.


--
-- TOC entry 2985 (class 0 OID 24748)
-- Dependencies: 212
-- Data for Name: reserva_ameni; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.reserva_ameni (id_reserva, fecha_dde, hora_dde, fecha_hasta, hora_hasta, edi_fk, uf_fk, ameni_fk) FROM stdin;
\.


--
-- TOC entry 2978 (class 0 OID 24641)
-- Dependencies: 205
-- Data for Name: unidad_funcional; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.unidad_funcional (id_uf, unidad_funcional, uf_tipo, piso, dpto, coprop_nombre, porc_a, porc_b, porc_c, porc_d, edif_fk) FROM stdin;
\.


--
-- TOC entry 2998 (class 0 OID 0)
-- Dependencies: 206
-- Name: amenities_id_ameni_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.amenities_id_ameni_seq', 1, false);


--
-- TOC entry 2999 (class 0 OID 0)
-- Dependencies: 202
-- Name: edificios_id_edif_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.edificios_id_edif_seq', 1, false);


--
-- TOC entry 3000 (class 0 OID 0)
-- Dependencies: 209
-- Name: reclamos_sugerencias_id_rec_sug_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.reclamos_sugerencias_id_rec_sug_seq', 1, false);


--
-- TOC entry 3001 (class 0 OID 0)
-- Dependencies: 211
-- Name: reserva_ameni_id_reserva_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.reserva_ameni_id_reserva_seq', 1, false);


--
-- TOC entry 3002 (class 0 OID 0)
-- Dependencies: 204
-- Name: unidad_funcional_id_uf_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.unidad_funcional_id_uf_seq', 1, false);


--
-- TOC entry 2836 (class 2606 OID 24705)
-- Name: amenities amenities_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.amenities
    ADD CONSTRAINT amenities_pk PRIMARY KEY (id_ameni);


--
-- TOC entry 2832 (class 2606 OID 24671)
-- Name: edificios edificios_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.edificios
    ADD CONSTRAINT edificios_pk PRIMARY KEY (id_edif);


--
-- TOC entry 2838 (class 2606 OID 24730)
-- Name: reclamos_sugerencias reclamos_sugerencias_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reclamos_sugerencias
    ADD CONSTRAINT reclamos_sugerencias_pk PRIMARY KEY (id_rec_sug);


--
-- TOC entry 2840 (class 2606 OID 24753)
-- Name: reserva_ameni reserva_ameni_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reserva_ameni
    ADD CONSTRAINT reserva_ameni_pk PRIMARY KEY (id_reserva);


--
-- TOC entry 2834 (class 2606 OID 24673)
-- Name: unidad_funcional unidad_funcional_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.unidad_funcional
    ADD CONSTRAINT unidad_funcional_pk PRIMARY KEY (id_uf);


--
-- TOC entry 2842 (class 2606 OID 24710)
-- Name: edif_ameni edif_ameni_fk; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.edif_ameni
    ADD CONSTRAINT edif_ameni_fk FOREIGN KEY (edi_fk) REFERENCES public.edificios(id_edif) ON DELETE RESTRICT;


--
-- TOC entry 2843 (class 2606 OID 24715)
-- Name: edif_ameni edif_ameni_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.edif_ameni
    ADD CONSTRAINT edif_ameni_fk_1 FOREIGN KEY (ameni_fk) REFERENCES public.amenities(id_ameni);


--
-- TOC entry 2844 (class 2606 OID 24731)
-- Name: reclamos_sugerencias reclamos_sugerencias_fk; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reclamos_sugerencias
    ADD CONSTRAINT reclamos_sugerencias_fk FOREIGN KEY (edi_fk) REFERENCES public.edificios(id_edif);


--
-- TOC entry 2845 (class 2606 OID 24736)
-- Name: reclamos_sugerencias reclamos_sugerencias_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reclamos_sugerencias
    ADD CONSTRAINT reclamos_sugerencias_fk_1 FOREIGN KEY (uf_fk) REFERENCES public.unidad_funcional(id_uf);


--
-- TOC entry 2846 (class 2606 OID 24754)
-- Name: reserva_ameni reserva_ameni_fk; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reserva_ameni
    ADD CONSTRAINT reserva_ameni_fk FOREIGN KEY (edi_fk) REFERENCES public.edificios(id_edif);


--
-- TOC entry 2847 (class 2606 OID 24759)
-- Name: reserva_ameni reserva_ameni_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reserva_ameni
    ADD CONSTRAINT reserva_ameni_fk_1 FOREIGN KEY (uf_fk) REFERENCES public.unidad_funcional(id_uf);


--
-- TOC entry 2848 (class 2606 OID 24764)
-- Name: reserva_ameni reserva_ameni_fk_2; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.reserva_ameni
    ADD CONSTRAINT reserva_ameni_fk_2 FOREIGN KEY (ameni_fk) REFERENCES public.amenities(id_ameni);


--
-- TOC entry 2841 (class 2606 OID 24681)
-- Name: unidad_funcional unidad_funcional_fk; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.unidad_funcional
    ADD CONSTRAINT unidad_funcional_fk FOREIGN KEY (edif_fk) REFERENCES public.edificios(id_edif) ON UPDATE CASCADE ON DELETE RESTRICT;


-- Completed on 2023-04-28 19:35:00

--
-- PostgreSQL database dump complete
--

