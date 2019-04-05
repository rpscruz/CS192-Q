
drop sequence if exists Queue_seq cascade;
drop table if exists Queue cascade;


drop sequence if exists Court_seq cascade;
drop table if exists Court cascade;


drop sequence if exists Player_seq cascade;
drop table if exists Player cascade;

drop sequence if exists ActivePlayer_seq cascade;
drop table if exists Player cascade;

drop sequence if exists Venue_seq cascade;
drop table if exists Venue cascade;


drop table if exists Match cascade;
drop sequence if exists Match_seq;
drop table if exists Match_Type cascade;

create sequence Venue_seq;
create table Venue(
    venue_id smallint not null default nextval('Venue_seq') primary key,
    venue_name varchar default nextval('Venue_seq'),
    creation_date timestamp not null default current_timestamp
);

create sequence Court_seq;
create table Court(
    court_id smallint not null default nextval('Court_seq') primary key,
    court_name varchar,
    venue_id smallint references Venue(venue_id),
    creation_date timestamp not null default current_timestamp
);

create sequence Player_seq;
create table Player(
    player_id smallint not null default nextval('Player_seq') primary key,
    last_name varchar,
    first_name varchar,
    player_level smallint,
    total_games smallint,
    total_win smallint,
    creation_date timestamp not null default current_timestamp
);

create sequence ActivePlayer_seq;
create table ActivePlayer(
    player_id smallint not null default nextval('Player_seq') primary key,
    last_name varchar,
    first_name varchar,
    player_level smallint,
    total_games smallint,
    total_win smallint,
    creation_date timestamp not null default current_timestamp
);

create table Match_Type(
    mt_id smallint not null default 0 primary key,
    type char(7)
);

create sequence Match_seq;
create table Match(
    m_id smallint not null default nextval('Match_seq') primary key,
    type smallint references Match_type,
    team1_p1 smallint not null references Player,
    team1_p2 smallint default null references Player,
    team2_p1 smallint not null references Player,
    team2_p2 smallint default null references Player,
    court_id smallint not null references Court,
    creation_date timestamp not null default current_timestamp,
    duration interval not null
);

insert into Match_Type values (0, 'Singles');
insert into Match_Type values (1, 'Doubles');


create view Queue as
    select * from Match
    where creation_date + duration > current_timestamp ;

create view Record as
    select * from Match
    where creation_date + duration < current_timestamp ;

-- select Court.court_name, Venue.venue_name from Court, Venue where Court.venue_id=Venue.venue_id;

