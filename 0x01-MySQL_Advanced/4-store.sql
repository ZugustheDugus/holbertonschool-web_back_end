-- script that creates a trigger that decreases the quantity of an item after adding a new order.
-- quanity in the table items CAN be negetaive

DELIMITER $$
CREATE TRIGGER checkout AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END $$
DELIMITER ;