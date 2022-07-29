CREATE OR REPLACE VIEW `role_view` AS
SELECT	r.name, f.name AS 'feature_name'
from 	role r
INNER JOIN
		_feature f
        ON f.id = r.feature_id

