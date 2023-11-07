# Dounake: Double Snake Versus Game

## Development
* Setup trước khi code:
```
pip install virtualenv
```
* Khi clone project về
```
virtualenv dounake_env
```
* Sau đó tiến hành source env cho project
    * Đối với macOS / Linux:
    ```
    source dounake_env/bin/activate
    ```
    * Đối với windows các bạn xem tại link [này](https://linuxhint.com/activate-virtualenv-windows/).

* Trước khi kết thúc phiên làm việc, vui lòng dùng lệnh sau để thoát khỏi env hiện tại, khi vào phiên làm việc tiếp theo source env cho project.
```
deactivate
```

* Khi có update mới trên project hãy cài đặt những thư viện mới nhất trên local:
```
pip install -r requirements.txt
```

* Ngoài ra khi code và trước khi tạo push code lên hãy sinh file requirements.txt cho các thành viên khác có thể biết được sử dụng thư viện mới.
```
pip freeze > requirements.txt
```

**QUAN TRỌNG**: Mọi người đọc thêm về [PEP 8](https://peps.python.org/pep-0008/) để viết code sạch sẽ hơn mọi người dễ làm việc với nhau hơn.

