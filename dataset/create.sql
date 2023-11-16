Example file: breast-cancer.csv

id,Class_name,Age,Menopause,Tumor_size,Inv_nodes,Node_caps,Deg_malig,Breast,Breast_quad,Irradiat
0,no-recurrence-events,30-39,premeno,30-34,0-2,no,3,left,left_low,no
1,no-recurrence-events,40-49,premeno,20-24,0-2,no,2,right,right_up,no



CREATE TABLE breast_cancer
(id serial,
Class_name varchar,
Age varchar,
Menopause varchar,
Tumor_size varchar,
Inv_nodes varchar,
Node_caps varchar,
Deg_malig integer,
Breast varchar,
Breast_quad varchar,
Irradiat varchar
);

COPY breast_cancer
FROM 'C:\work_prog\GEA_IKV_Prog_2\dataset\breast-cancer.csv'
DELIMITER ','
CSV HEADER;

AAHRAE database building_metadata.csv

site_id,building_id,primary_use,square_feet,year_built,floor_count
0,0,Education,7432,2008,
0,1,Education,2720,2004,

CREATE TABLE building_metadata
(site_id serial,
building_id integer,
primary_use varchar,
square_feet integer,
year_built integer,
floor_count integer
);

COPY building_metadata
FROM 'C:\work_prog\GEA_IKV_Prog_2\dataset\building_metadata.csv'
DELIMITER ','
CSV HEADER;