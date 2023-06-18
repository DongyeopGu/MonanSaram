from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# import schedule, time
############# AI
# import tensorflow.compat.v1 as tf, sys
# from tensorflow.compat.v1 import ConfigProto
# from tensorflow.compat.v1 import InteractiveSession
# import numpy as np
###############
import base64
import requests
from datetime import datetime
import os, re, glob
import numpy as np
import shutil
from tensorflow.keras.models import load_model

from accounts.models import User
from accounts.models import *
from .models import *
from .serializers import *

import cv2
from .faceswap.face_swap_2 import *

# 업로드 이미지 분석
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def analyze_image(request):

    def Dataization(img_path):
        image_w = 150
        image_h = 150
        img = cv2.imread(img_path)
        img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
        return (img/255)
    src = request.FILES['files']
    media_root = settings.MEDIA_ROOT+f'/users/{request.user}/'+ f'{src}'
    uploaded_image = HairImage.objects.create(upload_image=src, upload_user=request.user)
    image_serializer = HairImageSerializer(uploaded_image)
    test = [Dataization(media_root)]
    test = np.array(test)
    base_root = settings.BASE_DIR
    model = load_model(f'{base_root}/images/analyze/v6-2.h5')
    predict = model.predict(test)
    result = predict[0] * 100
    return Response({'result' : int(result), 'image': image_serializer.data})

# 결과 저장
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_score(request):
    print(request.data)
    hair_image = HairImage.objects.get(id=request.data['image'])
    hair_image.score = request.data['score']
    hair_image.save()
    image_serializer = HairImageSerializer(hair_image)
    return Response(status=200)

# 이미지 합성

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def compose_image(request):
    import random
    src = request.FILES['files']
    media_root = settings.MEDIA_ROOT+f'/users/{request.user}/'+ f'{src}'
    uploaded_image = ComposeImage.objects.create(upload_image=src, upload_user=request.user)
    image_name = request.data['path']
    default_image_dir = f'./media/default/{image_name}'
    try:
        base_src = request.FILES['base']
        base_image = ComposeImage.objects.create(upload_image=base_src, upload_user=request.user)
        default_image_dir = settings.MEDIA_ROOT+f'/users/{request.user}/'+ f'{base_src}'
        im1, landmarks1 = read_im_and_landmarks(default_image_dir)
        im2, landmarks2 = read_im_and_landmarks(media_root)

        M = transformation_from_points(landmarks1[ALIGN_POINTS],
                                    landmarks2[ALIGN_POINTS])

        mask = get_face_mask(im2, landmarks2)
        warped_mask = warp_im(mask, M, im1.shape)
        combined_mask = numpy.max([get_face_mask(im1, landmarks1), warped_mask],
                                axis=0)

        warped_im2 = warp_im(im2, M, im1.shape)
        warped_corrected_im2 = correct_colours(im1, warped_im2, landmarks1)

        output_im = im1 * (1.0 - combined_mask) + warped_corrected_im2 * combined_mask
        now_timestamp = datetime.timestamp(datetime.now())
        upload_path = settings.MEDIA_ROOT+'/users'+f'/{request.user}/{now_timestamp}.jpg'
        cv2.imwrite(upload_path, output_im)
        uploaded_image.delete()
        if base_image:
            base_image.delete()
        compose_image = ComposeImage.objects.create(upload_user=request.user, upload_image=f'{now_timestamp}.jpg')
        image_path = '/api/users'+f'/{request.user}/{now_timestamp}.jpg'
        return Response({'result': image_path})
    except:

        im1, landmarks1 = read_im_and_landmarks(default_image_dir)
        im2, landmarks2 = read_im_and_landmarks(media_root)

        M = transformation_from_points(landmarks1[ALIGN_POINTS],
                                    landmarks2[ALIGN_POINTS])

        mask = get_face_mask(im2, landmarks2)
        warped_mask = warp_im(mask, M, im1.shape)
        combined_mask = numpy.max([get_face_mask(im1, landmarks1), warped_mask],
                                axis=0)

        warped_im2 = warp_im(im2, M, im1.shape)
        warped_corrected_im2 = correct_colours(im1, warped_im2, landmarks1)

        output_im = im1 * (1.0 - combined_mask) + warped_corrected_im2 * combined_mask
        now_timestamp = datetime.timestamp(datetime.now())
        upload_path = settings.MEDIA_ROOT+'/users'+f'/{request.user}/{now_timestamp}.jpg'
        cv2.imwrite(upload_path, output_im)
        uploaded_image.delete()
        compose_image = ComposeImage.objects.create(upload_user=request.user, upload_image=f'{now_timestamp}.jpg')
        image_path = '/api/users'+f'/{request.user}/{now_timestamp}.jpg'
        return Response({'result': image_path})