CREATE TABLE
  public.user_table (
    id serial NOT NULL,
    created_at timestamp without time zone NOT NULL DEFAULT now(),
    user_login character varying(255) NOT NULL,
    user_pass character varying(255) NOT NULL,
    user_full_name character varying(255) NOT NULL,
    user_email character varying(255) NOT NULL,
    user_note character varying(255) NULL
  );

ALTER TABLE
  public.user_table
ADD
  CONSTRAINT user_table_pkey PRIMARY KEY (id)