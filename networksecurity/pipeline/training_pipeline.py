import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
)

from networksecurity.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
)

class TrainingPipeline:
    def __init__(self):
        self.trainig_pipeline_config=TrainingPipelineConfig()
        def start_data_ingestion(self):
            try:
                self.data_ingestion_config=DataIngestionConfig(training_pipeline_config=self.trainig_pipeline_config)
                logging.info("Start data ingestion")
                data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion.config)
                data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
                logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
                return data_ingestion_artifact

            except Exception as e:
                raise NetworkSecurityException(e,sys)
        def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact):
            try:
                self.data_validation_config=DataValidationConfig(training_pipeline_config=self.trainig_pipeline_config)
                logging.info("Start data validation")
                data_validation=DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=self.data_validation.config)
                data_validation_artifact=data_validation.initiate_data_validation()
                logging.info(f"Data validation completed and artifact: {data_validation_artifact}")
                return data_validation_artifact

            except Exception as e:
                raise NetworkSecurityException(e,sys)