from request.create import CreateUser
from request.delete import DeleteUser
from request.get import GetUsers
from request.put import UpdateUser
from status_codes.code import StatusCode


class Test(GetUsers, CreateUser, UpdateUser, DeleteUser, StatusCode):

    def test_get_users(self):
        get_response = GetUsers.get_users(self)
        assert get_response['code'] == 200

    def test_create_user(self):
        cr_response = CreateUser.create_user(self)
        assert cr_response['code'] == 201

    def test_update_user(self):
        up_response = UpdateUser.update_user(self)
        assert up_response['code'] == 200

    def test_delete_user(self):
        del_response = DeleteUser.delete_user(self)
        assert del_response['code'] == 204

    def test_status_code_400(self):
        response = StatusCode.status_code_400(self)
        assert response['code'] == 400

    def test_status_code_401(self):
        response = StatusCode.status_code_401(self)
        assert response['code'] == 401

    def test_status_code_404(self):
        response = StatusCode.status_code_404(self)
        assert response['code'] == 404

    def test_status_code_422(self):
        response = StatusCode.status_code_422(self)
        assert response['code'] == 422