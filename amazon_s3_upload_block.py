from nio.util.discovery import discoverable

from .amazon_s3_base_block import AmazonBase


@discoverable
class AmazonS3Upload(AmazonBase):

    def process_signals(self, signals):
        for signal in signals:
            try:
                self.logger.debug("Uploading {} to the {} bucket".format(
                    self.file_name(signal), self.bucket_name(signal)))
                self.client.upload_file(
                    self.file_name(signal).value,
                    self.bucket_name(signal),
                    self.key(signal))
            except:
                self.logger.exception("File upload failed")