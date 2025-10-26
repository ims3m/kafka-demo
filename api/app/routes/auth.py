from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix= '/auth')

@router.get('/test')
async def register_user_test():
    return {
        'message' : 'auth route is working!',
        'status_code' : 200
    }


@router.post('/register')
async def register_user():
    ...