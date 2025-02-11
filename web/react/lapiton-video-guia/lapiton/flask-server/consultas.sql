use juego;
DROP database juego;
CREATE database juego;
SHOW FULL tables;
DROP TABLE novedades;
select * from usuarios;
select * from juegos;
select * from ranking;
select * from novedades;
alter table novedades
modify column imagen LONGTEXT;
show create table novedades;

select usuario_fk,juego,categoria,max(puntaje) as maximo_puntaje
from ranking
group by usuario_fk,juego,categoria
order by maximo_puntaje desc;

SELECT *
from Juegos
WHERE nombre like 'El Tiburon';

SELECT *
from Juegos
where categoria LIKE (SELECT distinct categoria 
from juegos 
where nombre like 'El Tiburon');

DELETE FROM juegos
WHERE nombre like 'El Tiburon' and categoria like 'Accion';
DELETE FROM usuarios where nombre like 'josebueno';
INSERT INTO usuarios values(1,"jose","1234");
SET SQL_SAFE_UPDATES = 0;
delete from juegos;
INSERT INTO juegos values(1,'El Tiburon','Supervivencia','src/assets/fondoTiburonInicio.svg','2025-01-01');
INSERT INTO juegos values(2,'La Serpiente','Supervivencia','src/assets/campo-serpiente-1 1.svg','2025-01-01');
INSERT INTO juegos values(4,'El Tiburon','Accion','src/assets/fondoTiburonInicio.svg','2025-01-01');
INSERT INTO juegos values(4,'Duelo Vaquero','Accion','src/assets/vaquero.svg','2025-01-01');
INSERT INTO juegos values(5,'Policias y ladrones','Accion','src/assets/policias.svg','2025-01-01');
INSERT INTO juegos values(6,'Club de boxeo','Multijugador','src/assets/boxeo.svg','2025-01-01');
INSERT INTO juegos values(7,'Poker Texas','Multijugador','src/assets/poker.svg','2025-01-01');
INSERT INTO juegos values(8,'Ludo Stars','Multijugador','src/assets/ludo.svg','2025-01-01');
INSERT INTO juegos values(9,'Pirates Wars','Accion','src/assets/piratas.svg','2025-01-01');
