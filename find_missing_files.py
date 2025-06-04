generated_filenames = [
    "applocker.md",
    "browser_protection.md",
    "microsoft_defender_application_guard.md",
    "microsoft_vulnerable_driver_block.md",
    "smart_app_control.md",
    "trusted_signing.md",
    "virtualization_based_integrity_vbi.md",
    "windows_sandbox.md",
    "windows_subsystem_for_linux_wsl.md",
    "wsl_app_isolation.md",
    "microsoft_entra_id.md",
    "microsoft_entra_private_access.md",
    "microsoft_entra_internet_access.md",
    "azure_attestation_service.md",
    "microsoft_defender_for_endpoint.md",
    "cloud_native_device_management.md",
    "microsoft_intune.md",
    "windows_enrollment_attestation.md",
    "microsoft_cloud_pki.md",
    "enterprise_privilege_management_epm.md",
    "mobile_application_management_mdm.md",
    "security_baselines.md",
    "local_administrator_password_solution_laps.md",
    "windows_autopilot.md",
    "windows_update_for_business.md",
    "windows_autopatch.md",
    "windows_hotpatch.md",
    "onedrive_for_work_or_school.md",
    "universal_print.md",
    "microsoft_account.md",
    "find_my_device.md",
    "onedrive_for_personal_use.md",
    "family_safety.md",
    "personal_vault.md",
    "configuration_lock.md",
    "direct_memory_access_dma_protection.md",
    "hardware_enforced_stack_protection.md",
    "hypervisor_enforced_bug_reporting_hebr.md",
    "hypervisor_protected_code_integrity_hvci.md",
    "kernel_data_memory_entropy_dma_protection.md",
    "microsoft_secure_process_protections.md",
    "secure_boot.md",
    "trusted_platform_module_tpm_2_0.md",
    "virtualization_based_security_vbs.md",
    "access_management_and_control_uac.md",
    "account_lockout_policy.md",
    "azure_ad_join.md",
    "credential_guard.md",
    "enhanced_phishing_protection.md",
    "enhanced_sign_in_security.md",
    "fido2.md",
    "microsoft_authenticator.md",
    "microsoft_privacy_statements_and_controls.md",
    "privacy_controls.md",
    "privacy_resource_usage.md",
    "remote_credential_guard.md",
    "smart_card.md",
    "token_protection.md",
    "vbs_key_protection.md",
    "windows_diagnostic_data_processor_configuration.md",
    "windows_hello.md",
    "windows_hello_for_business.md",
    "webauthn.md",
    "5g_and_esim.md",
    "bitlocker.md",
    "bitlocker_to_go.md",
    "certificates.md",
    "code_signing_and_integrity.md",
    "config_refresh.md",
    "controlled_folder_access.md",
    "cryptography.md",
    "device_health_attestation.md",
    "domain_name_system_dns_security.md",
    "email_encryption.md",
    "encrypted_file_system_efs.md",
    "encrypted_hard_drive.md",
    "exploit_protection.md",
    "internet_protocol_security_ipsec.md",
    "kiosk_mode.md",
    "microsoft_defender_antivirus.md",
    "microsoft_defender_application_guard.md",
    "microsoft_defender_for_business.md",
    "network_access_protection.md",
    "personal_data_encryption.md",
    "rust_for_windows.md",
    "server_message_block_smb_for_remote_connections.md",
    "tamper_protection.md",
    "transport_layer_security_tls.md",
    "wi_fi_protection.md",
    "windows_firewall.md",
    "windows_protected_process.md",
    "windows_security_app.md",
    "windows_security_policy_settings_and_auditing.md",
    "common_criteria_cc.md",
    "devdivsecops.md",
    "federal_information_processing_standard_fips.md",
    "microsoft_offensive_research_and_security_engineering_morse.md",
    "secure_future_initiative_sfi.md",
    "security_development_lifecycle_sdl.md",
    "software_bill_of_materials_sbom.md",
    "windows_kernel_and_microsoft_bug_bounty_programs.md",
    "windows_software_development_kit_sdk.md"
]

# existing_files_output is the raw string from ls()
# which includes the directory path and an empty line sometimes.
existing_files_raw = [
    "posts/md/identity_access_management_and_control_uac.md",
    "posts/md/windows_hello_enhanced_sign_in_security.md"
]

# Extract just the filenames
existing_files = set()
for f_path in existing_files_raw:
    if f_path.strip(): # Ensure not empty line
        parts = f_path.split('/')
        if len(parts) > 0:
            existing_files.add(parts[-1])


# Using a set for efficient lookup
generated_filenames_set = set(generated_filenames)

files_to_create = list(generated_filenames_set - existing_files)
# Sort for consistent output, helpful for review
files_to_create.sort()

if not files_to_create:
    print("All generated Markdown files already exist in posts/md/.")
else:
    print("The following Markdown files need to be created in posts/md/:")
    for f_name in files_to_create:
        print(f_name)
