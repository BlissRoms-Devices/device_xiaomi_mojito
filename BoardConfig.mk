#
# Copyright (C) 2021 The PixelExperience Project
#
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/xiaomi/mojito

# A/B
AB_OTA_UPDATER := true
BOARD_USES_RECOVERY_AS_BOOT := true

AB_OTA_PARTITIONS += \
    boot \
    dtbo \
    odm \
    product \
    system \
    system_ext \
    vbmeta \
    vbmeta_system \
    vendor \
    vendor_boot

# Audio
TARGET_PROVIDES_AUDIO_EXTNS := true

# Board
TARGET_BOARD_INFO_FILE := $(DEVICE_PATH)/board-info.txt

# Display
TARGET_SCREEN_DENSITY := 440

# Init
TARGET_INIT_VENDOR_LIB := //$(DEVICE_PATH):libinit_mojito

# Kernel
TARGET_KERNEL_CONFIG := vendor/mojito_defconfig vendor/debugfs.config
TARGET_KERNEL_SOURCE := kernel/xiaomi/mojito
TARGET_KERNEL_ADDITIONAL_FLAGS := \
    LLVM=1 \
    LLVM_IAS=1

# OTA assert
TARGET_OTA_ASSERT_DEVICE := mojito,sunny

# Properties
TARGET_VENDOR_PROP += $(DEVICE_PATH)/vendor.prop

# Inherit from sm6150-common
include device/xiaomi/sm6150-common/BoardConfigCommon.mk

# Inherit from the proprietary version
include vendor/xiaomi/mojito/BoardConfigVendor.mk

# Inherit from proprietary files for Leica Camera
-include vendor/xiaomi/mojito-leicacamera/BoardConfigVendor.mk
