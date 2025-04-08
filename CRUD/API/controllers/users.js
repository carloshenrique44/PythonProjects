import { db } from "../db";

export const getUsers = (_, res) => {
    const q = "Select * from usuarios";

    db.query(q, (err, data) => {
        if (err) return res.json(err);

        return res.status(200).json(data);
 });
};

