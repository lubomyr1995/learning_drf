import os
from uuid import uuid1


class FileService:
    @staticmethod
    def upload_car_photo(instance, file: str, ) -> str:
        ext = file.split('.')[-1]
        return os.path.join('car_photos', f'{uuid1()}.{ext}')
