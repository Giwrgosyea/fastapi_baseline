from ..util.db.decorator import mongodb_access
from ..model.park_model import Park
from motor.errors import DoesNotExist, FieldDoesNotExist, ValidationError
from pymongo.errors import DuplicateKeyError
from ..log.logger import Logger

my_logger = Logger(__name__)
logger = my_logger.get_logger()


@mongodb_access
async def post_new_park(data):
    try:
        try:
            park = Park.objects.get(asset_id=data["asset_id"])
        except DoesNotExist:
            try:
                new_park = Park(asset_id=data["asset_id"], park_name=data["park_name"])
                new_park.save()

                logger.info(f'{data["asset_id"]} Park Successfully inserted')
                response_object = {
                    "status": "ok",
                    "message": "All Park Successfully inserted",
                }
                return response_object, 201
            except FieldDoesNotExist as e:
                logger.error(e)
                response_object = {"status": "fail", "message": e}
                return response_object, 400
            except DuplicateKeyError as e:
                logger.error(e)
                response_object = {"status": "fail", "message": e}
                return response_object, 400
            except KeyError as e:
                logger.error(e)
                response_object = {"status": "fail", "message": e}
                return response_object, 400
            except ValidationError as e:
                logger.error(e)
                response_object = {"status": "fail", "message": e}
                return response_object, 400
            except Exception as ex:
                logger.exception(ex)
                response_object = {"status": "fail", "message": ex}
                return response_object, 400

    except DuplicateKeyError as e:
        logger.error(e)
        response_object = {"status": "fail", "message": e}
        return response_object, 400
    except KeyError as e:
        logger.error(e)
        response_object = {"status": "fail", "message": e}
        return response_object, 400
    except ValidationError as e:
        logger.error(e)
        response_object = {"status": "fail", "message": e}
        return response_object, 400
    except FieldDoesNotExist as e:
        logger.error(e)
        response_object = {"status": "fail", "message": e}
        return response_object, 400
    except Exception as ex:
        logger.exception(ex)
        response_object = {"status": "fail", "message": ex}
        return response_object, 400
