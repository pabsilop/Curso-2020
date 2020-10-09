-- create table producto (id bigint not null, nombre varchar(255), precio double not null, unidades_en_stock integer not null, primary key (id))

INSERT INTO PRODUCTO (ID, NOMBRE, PRECIO, UNIDADES_EN_STOCK, DESCRIPCION)
VALUES (NEXTVAL('hibernate_sequence'), 'Botellines',9.0, 100, 'Los botellines más frios a este lado de Triana');

INSERT INTO PRODUCTO (ID, NOMBRE, PRECIO, UNIDADES_EN_STOCK, DESCRIPCION)
VALUES (NEXTVAL('hibernate_sequence'), 'Sobre de 100g Jamón Ibérico',10.5, 60, 'Jamón de pata negra no tan negra');

INSERT INTO PRODUCTO (ID, NOMBRE, PRECIO, UNIDADES_EN_STOCK, DESCRIPCION)
VALUES (NEXTVAL('hibernate_sequence'), 'Regañás de Cañada Rosal', 3.25, 120,'Ideales para que el jamon pase correctamente');

INSERT INTO PRODUCTO (ID, NOMBRE, PRECIO, UNIDADES_EN_STOCK, DESCRIPCION)
VALUES (NEXTVAL('hibernate_sequence'), 'Regañás de Cañada Rosal', 3.25, 120,'Ideales para que el jamon pase correctamente');

