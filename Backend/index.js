const fs = require('fs');
const jsonServer = require('json-server');
const path = require('path');

const server = jsonServer.create()

const router = jsonServer.router(path.resolve(__dirname, 'db.json'));

server.use(jsonServer.defaults({}))
server.use(jsonServer.bodyParser)

// Нужно для небольшой задержки, чтобы запрос проходил не мгновенно, имитация реального апи
server.use(async (req, res, next) => {
    await new Promise((res) => {
        setTimeout(res, 800)
    })
    next()
})
// Эндпоинт для логина
server.post('/login', (req, res) => {
    try {
        const { email, password } = req.body;
        const db = JSON.parse(fs.readFileSync(path.resolve(__dirname, 'db.json'), 'UTF-8'));
        const { users = [] } = db;

        const userFromBd = users.find(
            (user) => user.email === email && user.password === password,
        );

        if (userFromBd) {
            return res.json(userFromBd)
        }

        return res.status(403).json({ message: 'User not found' })
    } catch (e) {
        console.log(e);
        return res.status(500).json({ message: e.message })
    }
});
server.post('/users', (req, res) => {
    try {
        const { email, password } = req.body;
        const db = JSON.parse(fs.readFileSync(path.resolve(__dirname, 'db.json'), 'UTF-8'));
        const { users = [] } = db;

        // Генерируем уникальный идентификатор для нового пользователя
        const userId = users.length > 0 ? Math.max(...users.map((user) => user.id)) + 1 : 1

        // Создаем нового пользователя
        const newUser = {
            id: userId,
            email,
            password
        }
        // Добавляем нового пользователя в массив пользователей
        users.push(newUser)

        // Обновляем данные в JSON-файле
        fs.writeFileSync(path.resolve(__dirname, 'db.json'), JSON.stringify(db, null, 2), 'UTF-8')

        return res.json(newUser)
    } catch (e) {
        return res.status(500).json({ message: e.message });
    }
})
server.post('/profile', (req, res) => {
    try {
        const { id, name, lastname } = req.body;
        const db = JSON.parse(fs.readFileSync(path.resolve(__dirname, 'db.json'), 'UTF-8'));
        const { profile = [] } = db;

        // Проверяем, существует ли профиль с указанным id
        const existingProfile = profile.find((item) => item.id === id);
        if (existingProfile) {
            return res.status(400).json({ message: 'Profile with the same id already exists' });
        }

        // Создаем новый профиль
        const newProfile = {
            id: String(id),
            name,
            lastname,
        };

        // Добавляем новый профиль в массив профилей
        profile.push(newProfile);

        // Обновляем данные в JSON-файле
        fs.writeFileSync(path.resolve(__dirname, 'db.json'), JSON.stringify(db, null, 2), 'UTF-8');

        return res.json(newProfile);
    } catch (e) {
        console.log(e);
        return res.status(500).json({ message: e.message });
    }
});
server.get('/profile/:id', (req, res) => {
    try {
        const { id } = req.params

        // Проверяем, авторизирован ли пользователь (проверьте вашу логику проверки авторизации)
        if (!req.headers.authorization) {
            return res.status(403).json({ message: 'Not authorized' });
        }

        const db = JSON.parse(fs.readFileSync(path.resolve(__dirname, 'db.json'), 'UTF-8'));
        const { profile = [] } = db;

        // Находим профиль по указанному id
        const foundProfile = profile.find((item) => item.id === id);

        if (foundProfile) {
            return res.json(foundProfile);
        } else {
            return res.status(404).json({ message: 'Profile not found' });
        }
    } catch (e) {
        console.log(e);
        return res.status(500).json({ message: e.message });
    }
});
// проверяем, авторизован ли пользователь
// eslint-disable-next-line
server.use((req, res, next) => {
    if (!req.headers.authorization) {
        return res.status(403).json({ message: 'AUTH ERROR' });
    }

    next();
});

server.use(router);

// запуск сервера
server.listen(8000, () => {
    console.log('server is running on 8000 port');
});
