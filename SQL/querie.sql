SELECT *
FROM calendario as C 
LEFT JOIN metro AS M ON C.FECHA=M.FECHA
LEFT JOIN (
    SELECT FECHA,
            PROVINCIA,
            AVG(TMEND)      AS TMEND,
            AVG(PREC)       AS PREC,
            AVG(TMIN)       AS TMIN,
            AVG(HORATMIN)   AS HORATMIN,
            AVG(TMAX)       AS TMAX,
            AVG(HORATMAX)   AS HORATMAX,
            AVG(DIR)        AS DIR,
            AVG(VELMEDIA)   AS VELMEDIA,
            AVG(RACHA)      AS RACHA,
            AVG(HORARACHA)  AS HORARACHA,
            AVG(PRESMAX)    AS PRESMAX,
            AVG(HORAPRESMAX) AS HORAPRESMAX,
            AVG(PRESMIN)    AS PRESMIN ,
            AVG(HORAPRESMIN) AS HORAPRESMIN
    FROM clima 
    GROUP BY FECHA, PROVINCIA)
 AS C ON M.FECHA=C.FECHA