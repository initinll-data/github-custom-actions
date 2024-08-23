const core = require('@actions/core');
const github = require('@actions/github');
const exec = require('@actions/exec');

function run() {
    core.notice('Hello from my custom Javascript Actions!');
    // 1) Get action input values
    const bucket = core.getInput('bucket', { required: true });
    const bucketRegion = core.getInput('bucket-region', { required: true });
    const distFolder = core.getInput('dist-folder', { required: true });

    // 2) Display input values
    core.notice(`action: ${github.context.action}`);
    core.notice(`bucket: ${bucket}`);
    core.notice(`bucketRegion: ${bucketRegion}`);
    core.notice(`distFolder: ${distFolder}`);

    // 3) upload files to S3
    // const s3Uri = `s3://${bucket}`;
    // exec.exec(`ws s3 sync ${distFolder} ${s3Uri} --region ${bucketRegion}`);
    core.notice('Upload to S3 complete!');
}

run();

