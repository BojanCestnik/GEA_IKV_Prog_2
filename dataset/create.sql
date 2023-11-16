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