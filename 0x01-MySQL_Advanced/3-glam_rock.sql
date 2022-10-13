-- list all bands with Glam rock as their style rank by longetivity
-- column names must be band_name and lifespan
-- you should use attributes formed and split for computer lifespan

SELECT band_name, IFNULL(split, 2020) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam Rock%'
ORDER BY lifespan DESC;
